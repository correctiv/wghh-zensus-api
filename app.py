import json
import os
from flask import Flask, g, jsonify, request

from database import query_db
from geocoder import geocode


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({
    'DATABASE': os.path.join(app.root_path, 'data.db')
})
app.config.from_envvar('SETTINGS', silent=True)


@app.route('/')
def api():
    loc = geocode(request.args['q'])
    if loc:
        res = query_db(loc.longitude, loc.latitude)
        if res:
            return jsonify({'data': json.loads(res[0])})
    return jsonify({'data': None})


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
