from app import app
from flask import render_template
from app.models import * # NEW ADDITION PROPOSED

@app.route('/')
def index():
    return render_template('base.html')

# NEW ADDITION PROPOSED - ALL CODE BELOW THIS LINE
@app.route('/event-list/<state>')
def show_event_list(state):
    state_events = events.query.join(locations).filter(locations.state==state).all()
    events_to_list = state_events
    return render_template('events.html', events=state_events, state=state)
    
@app.route('/event/<id>')
def show_event(id):
    event = events.query.first()
    return render_template('event.html',event_shown=event)