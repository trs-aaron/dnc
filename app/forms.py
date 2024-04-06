from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

from app.models import *

class RSVPForm(FlaskForm):

    def __init__(self, event, location):
        super().__init__()
        self.event = event
        self.location = location

    event: events = None
    location: locations = None
    family_name = StringField('Family Name', validators=[DataRequired()])
    given_name = StringField('Given Name', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired()])
    phone = StringField('Phone', validators=[Optional()])

    def submit(self):
        rsvps.rsvp_to_event(
            location_id=self.location.id,
            family_name=self.family_name.data,
            given_name=self.given_name.data,
            email=self.email.data,
            phone=self.phone.data
        )
