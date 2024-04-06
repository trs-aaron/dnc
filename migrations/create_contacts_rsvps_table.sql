create table contacts (
    id integer CONSTRAINT PK_contacts PRIMARY KEY,
    modified_date timestamp without time zone,
    created_date timestamp without time zone,
    family_name character varying,
    given_name character varying,
    phone character varying,
    email character varying
);

create table rsvps (
    id integer CONSTRAINT PK_rsvps PRIMARY KEY,
    modified_date timestamp without time zone,
    created_date timestamp without time zone,
    attendee_id integer not null,
    location_id integer not null,
    attended BOOLEAN NOT NULL CHECK (rsvps.attended IN (0, 1)),
    FOREIGN KEY (attendee_id) REFERENCES contacts (id),
    FOREIGN KEY (location_id) REFERENCES contacts (id)
);
