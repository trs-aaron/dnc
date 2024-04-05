from app import app
from flask import jsonify, request
from app.models import *


@app.route('/api/events/')
def get_events():
    all_events = events.query.all()
    result = events_schema.dump(all_events)
    return jsonify(result)

@app.route('/api/events/<id>')
def event_detail(id):
    event = events.query.filter_by(id=id).first()
    return event_schema.jsonify(event)

