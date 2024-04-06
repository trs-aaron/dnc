from app import app
from flask import redirect, render_template, request
from app.forms import *
from app.models import * # NEW ADDITION PROPOSED

@app.route('/')
def index():
    return render_template('base.html')

# NEW ADDITION PROPOSED - ALL CODE BELOW THIS LINE
@app.route('/event-list/<state>/')
def show_event_list(state):
    state_events = events.query.join(locations).filter_by(state=state).all()
    return render_template('events.html', events=state_events, state=state)
    
@app.route('/event/<id>/')
def show_event(id):
    event = events.query.filter_by(id=id).join(locations).first()
    return render_template('event.html', event=event, locations=event.locations)

@app.route('/event/<event_id>/<location_id>/')
def show_location(event_id, location_id):
    location = locations.query.filter_by(id=location_id).first()
    is_attending = True if request.args.get('isAttending') else False
    return render_template('event.html', event=location.event, locations=[location], is_attending=is_attending)

@app.route('/event/<event_id>/<location_id>/rsvp/', methods=['GET', 'POST'])
def show_rsvp(event_id, location_id):
    location = locations.query.filter_by(id=location_id).first()
    form = RSVPForm(event=location.event, location=location)

    if form.validate_on_submit():
        form.submit()
        return redirect('/event/{event_id}/{location_id}?isAttending=1'.format(event_id=event_id, location_id=location_id))

    return render_template('rsvp.html', form=form)
