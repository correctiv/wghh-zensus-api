import json
import os
from flask import Flask, g, jsonify, request, Response

from database import init_db
from lookup import query, suggest as _suggest


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({
    'DATABASE': os.path.join(app.root_path, 'data.db')
})
app.config.from_envvar('SETTINGS', silent=True)


@app.route('/')
def api():
    if 'street' not in request.args or 'nr' not in request.args:
        return Response('<h1>400</h1>', status=400)
    data, match = query(request.args)
    if data:
        return jsonify({
            'data': json.loads(data),
            'match': match
        })
    return jsonify({'data': None})


@app.route('/suggest')
def suggest():
    if 'q' not in request.args:
        return Response('<h1>400</h1>', status=400)
    data = _suggest(request.args['q'])
    return jsonify({'data': data})


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')
