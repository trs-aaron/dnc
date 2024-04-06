from app import app
from flask import jsonify, request
from app.models import *


@app.route('/api/contacts/')
def get_contacts():
    all_contacts = contacts.query.all()
    result = contacts_schema.dump(all_contacts)
    return jsonify(result)

@app.route('/api/contacts/<id>')
def contact_detail(id):
    contact = contacts.query.filter_by(id=id).first()
    return event_schema.jsonify(contact)

@app.route('/api/events/')
def get_events():
    all_events = events.query.all()
    result = events_schema.dump(all_events)
    return jsonify(result)

@app.route('/api/events/<id>')
def event_detail(id):
    event = events.query.filter_by(id=id).first()
    return event_schema.jsonify(event)

@app.route('/api/locations/')
def get_locations():
    all_locations = locations.query.all()
    result = locations_schema.dump(all_locations)
    return jsonify(result)

@app.route('/api/locations/<id>')
def location_detail(id):
    event = locations.query.filter_by(id=id).first()
    return location_schema.jsonify(event)

@app.route('/api/rsvps/')
def get_rsvps():
    all_rsvps = rsvps.query.all()
    result = rsvps_schema.dump(all_rsvps)
    return jsonify(result)

@app.route('/api/rsvps/<id>', methods=['GET'])
def rsvp_detail(id):
    rsvp = rsvps.query.filter_by(id=id).first()
    return rsvp_schema.jsonify(rsvp)
