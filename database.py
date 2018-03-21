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
