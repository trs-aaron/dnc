from sqlalchemy.sql import func
from typing import List

from app import db, ma

# There are no intentional bugs in this file (but you can certainly add to it if you want)

class contacts(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=func.now())
    modified_date = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    family_name = db.Column(db.String(120))
    given_name = db.Column(db.String(120))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(255))
    rsvps: db.Mapped[List["rsvps"]] = db.relationship("rsvps", back_populates="attendee")

    def __repr__(self):
        return "{} - id {}".format(self.name, self.id)

class events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(250))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    official = db.Column(db.Boolean)
    visibility = db.Column(db.String(120))
    guests_can_invite_others = db.Column(db.Boolean)
    modified_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    participant_count = db.Column(db.Integer)
    reason_for_private = db.Column(db.String(250))
    order_email_template = db.Column(db.Text)
    name = db.Column(db.String(120))
    locations: db.Mapped[List["locations"]] = db.relationship("locations", back_populates="event") # An event can have multiple locations

    def __repr__(self):
        return "{} - id {}".format(self.name, self.id)

class locations(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event: db.Mapped["events"] = db.relationship("events", back_populates="locations")
    address_type = db.Column(db.String(120))
    contact_phone = db.Column(db.String(15))
    primary = db.Column(db.Boolean)
    contact_email = db.Column(db.String(255))
    contact_family_name = db.Column(db.String(120))
    contact_given_name = db.Column(db.String(120))
    host_given_name = db.Column(db.String(120))
    timezone = db.Column(db.String(50))
    city = db.Column(db.String(120))
    locality = db.Column(db.String(120))
    state = db.Column(db.String(50))
    address_type = db.Column(db.String(120))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    accuracy = db.Column(db.String(120))
    address1 = db.Column(db.String(120))
    address2 = db.Column(db.String(120))
    postal_code = db.Column(db.String(12))
    country = db.Column(db.String(120))
    modified_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    number_spaces_remaining = db.Column(db.Integer)
    spaces_remaining = db.Column(db.Boolean)
    name = db.Column(db.String(250))
    rsvps: db.Mapped[List["rsvps"]] = db.relationship("rsvps", back_populates="location")

    def __repr__(self):
        return "{} - id {}".format(self.name, self.id)

class rsvps(db.Model):
    __tablename__ = "rsvps"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=func.now())
    modified_date = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    attended = db.Column(db.Boolean, default=False)
    attendee_id = db.Column(db.Integer, db.ForeignKey('contacts.id'))
    attendee: db.Mapped["contacts"] = db.relationship("contacts", back_populates="rsvps")
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location: db.Mapped["locations"] = db.relationship("locations", back_populates="rsvps")

    @classmethod
    def rsvp_to_event(cls, location_id, family_name, given_name, email, phone=None):
        location = locations.query.filter_by(id=location_id).first()

        if location.spaces_remaining:

            if location.number_spaces_remaining is not None:
                location.number_spaces_remaining = (location.number_spaces_remaining - 1)
                location.spaces_remaining = (location.number_spaces_remaining > 0)

            contact = contacts.query.filter_by(
                family_name=family_name,
                given_name=given_name,
                email=email,
                phone=phone
            ).first()

            if not contact:
                contact = contacts(
                    family_name=family_name,
                    given_name=given_name,
                    email=email,
                    phone=phone
                )

            rsvp = rsvps(
                location_id=location.id
            )

            contact.rsvps.append(rsvp)

            db.session.add(contact)
            db.session.add(rsvp)
            db.session.commit()

    def __repr__(self):
        return "{} - id {}".format(self.name, self.id)

# Schemas for existing API using an API library (marshmallow)
class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = contacts

    _links = ma.Hyperlinks({
        'self': ma.URLFor('contact_detail', id='<id>'),
        'collection': ma.URLFor('get_contacts')
    })

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = events

    _links = ma.Hyperlinks({
        'self': ma.URLFor('event_detail', id='<id>'),
        'collection': ma.URLFor('get_events')
    })

event_schema = EventSchema()
events_schema = EventSchema(many=True)

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = locations

    _links = ma.Hyperlinks({
        'self': ma.URLFor('location_detail', id='<id>'),
        'collection': ma.URLFor('get_locations')
    })

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

class RsvpSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = rsvps

    _links = ma.Hyperlinks({
        'self': ma.URLFor('rsvp_detail', id='<id>'),
        'collection': ma.URLFor('get_rsvps')
    })

rsvp_schema = RsvpSchema()
rsvps_schema = RsvpSchema(many=True)
