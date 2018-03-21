import json
import os
from flask import Flask, g, jsonify, request, Response

from lookup import query


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


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
