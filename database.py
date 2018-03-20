import sqlite3
from flask import current_app, g


def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(current_app.config['DATABASE'])


def get_db():
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def query_db(lon, lat):
    db = get_db()
    cursor = db.execute(
        'select data from grids where (%s between x1 and x2) and (%s between y3 and y1)' % (lon, lat)
    )
    return cursor.fetchone()
