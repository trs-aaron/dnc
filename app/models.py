from app import db, ma

# There are no intentional bugs in this file (but you can certainly add to it if you want)

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
    locations = db.relationship("locations") # An event can have multiple locations

    def __repr__(self):
        return "{} - id {}".format(self.name,self.id)

class locations(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
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

    def __repr__(self):
        return "{} - id {}".format(self.name,self.id)


# Schemas for existing API using an API library (marshmallow)
class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = events

    _links = ma.Hyperlinks({
        'self': ma.URLFor('event_detail', id='<id>'),
        'collection': ma.URLFor('get_events')
    })

event_schema = EventSchema()
events_schema = EventSchema(many=True)
