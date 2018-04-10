import subprocess
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


def init_db():
    # db = get_db()
    # with current_app.open_resource('init_db.sql', mode='r') as f:
    #     script = f.read().strip()
    # db.cursor().executescript(script)
    # db.commit()
    subprocess.run(['sqlite3', 'data.db'], stdin=current_app.open_resource('init_db.sql'))
