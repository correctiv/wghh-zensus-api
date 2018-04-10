import re
from flask import current_app

from database import get_db
from geocoder import geocode


def _query_data(lon, lat):
    db = get_db()
    cursor = db.execute(
        'select data from grids where (? between x1 and x2) and (? between y3 and y1)',
        (lon, lat)
    )
    res = cursor.fetchone()
    if res:
        return res[0]


def _query_adress(street_name, housenr):
    db = get_db()
    cursor = db.execute(
        'select lon, lat from adresses where street_name=? and housenr=?',
        (street_name, housenr)
    )
    return cursor.fetchone()


def _query_street(street_name):
    db = get_db()
    cursor = db.execute(
        'select lon, lat from streets where street_name=?',
        (street_name,)
    )
    return cursor.fetchone()


def query(args):
    street_name = args['street'].lower()
    housenr = re.sub('[^0-9]', '', args['nr'])
    adress = ' '.join((args['street'], args['nr']))
    match = None

    # try adress lookup in our database
    coords = _query_adress(street_name, housenr)

    if coords:
        data = _query_data(*coords)
        if data:
            match = 'exact'
            return data, match

        # try street name lookup
        coords = _query_street(street_name)
        data = _query_data(*coords)
        if data:
            match = 'street'
            return data, match

    else:
        # try street name lookup
        coords = _query_street(street_name)
        if coords:
            data = _query_data(*coords)
            if data:
                match = 'street'
                return data, match

        # geocode
        if current_app.debug:
            print('geocoding "%s" ...' % adress)
        loc = geocode(adress)
        if loc:
            data = _query_data(loc.longitude, loc.latitude)
            if data:
                match = 'geocode'
                return data, match

        if current_app.debug:
            print('can\'t find results for "%s"' % adress)

    return None, None


def suggest(value):
    value = value.lower().strip()
    if value:
        db = get_db()
        cursor = db.execute(
            'select street_name from streets where street_name like ?',
            (value + '%',)
        )
        data = cursor.fetchall()
        return [d[0].title() for d in data]
    return []
