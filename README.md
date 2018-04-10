# wghh-zensus-api

A simple [flask](http://flask.pocoo.org/) app that serves an api endpoint to
obtain flats ownership statistics for addresses in Hamburg, Germany.

It turns a given adress into coordinates and then looks up the corresponding
100m square grid from the [Zensus11 Wohnungen &
Gebäude](https://www.zensus2011.de/SharedDocs/Aktuelles/Ergebnisse/DemografischeGrunddaten.html?nn=3065474)
dataset.

To obtain the coordinates, it first looks into the [ALKIS Adressen
Hamburg](http://suche.transparenz.hamburg.de/dataset/alkis-adressen-hamburg7)
dataset.

As a fallback, it uses [Nominatim](https://nominatim.openstreetmap.org/) as a
geocoder to obtain coordinates.

It also provides an autocomplete endpoint for suggesting street names.

## install

    pip install -r requirements.txt

## local run

    FLASK_DEBUG=1 FLASK_APP=app.py flask run

this will fire up a local webserver at [127.0.0.1:5000](http://127.0.0.1:500)

## query

The endpoint expects two self-explanatory `GET` parameters:
- street
- nr

It returns a `json` dictionary with the key `data` that is either `null` or
full of data plus an additional key `match` that shows info about the exactness
of the result

## suggest

the endpoint `/suggest` expects a `GET` parameter named `q`. It will search the
database against street names starting with this value.

It returns a `json` dictionary with the key `data` that is a list of street
names (that may be empty if nothing is found).

## examples

Query for "Sievekingsallee 3":

[http://127.0.0.1:5000/?street=Sievekingsallee&nr=3](http://127.0.0.1:5000/?street=Sievekingsallee&nr=3)

the result:

```json
{
  "data": {
    "flats_cooperative_owned": 26,
    "flats_cooperative_owned_q": 21,
    "flats_ngo_church_owned": 0,
    "flats_ngo_church_owned_q": 0,
    "flats_other_private_company_owned": 0,
    "flats_other_private_company_owned_q": 0,
    "flats_private_company_owned": 0,
    "flats_private_company_owned_q": 0,
    "flats_private_owned": 94,
    "flats_private_owned_q": 78,
    "flats_public_body_owned": 0,
    "flats_public_body_owned_q": 0,
    "flats_state_owned": 0,
    "flats_state_owned_q": 0,
    "flats_total": 120,
    "id": "100mN33834E43253"
  },
  "match": "street"
}
```

Autocomplete street names starting with "müg":

[http://127.0.0.1:5000/suggest?q=müg](http://127.0.0.1:5000/suggest?q=müg)

the result:

```json
{
  "data": [
    "M\u00fcggenburg",
    "M\u00fcggenburger Hauptdeich",
    "M\u00fcggenburger Stra\u00dfe",
    "M\u00fcggenkampstra\u00dfe",
    "M\u00fcggenloch"
  ]
}
```
