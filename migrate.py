__author__ = 'mrkaiser'

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
                                                       "mysql+mysqlconnector://username:password@localhost/database")

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, db.Sequence('person_id_seq'), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    url = db.Column(db.String(150))
    about = db.Column(db.String(400))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)

    def __repr__(self):
        return "Person<first_name=%s,last_name=%s,url=%s" % (self.first_name, self.last_name, self.url)


class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, db.Sequence('track_id_seq'), primary_key=True)
    name = db.Column(db.String(50))
    tagline = db.Column(db.String(140))
    url = db.Column(db.String(300))
    desc = db.Column(db.String(500))
    director = db.relationship('Person', backref='tracks')
    events = db.relationship('Event', backref='tracks')

    def __repr__(self):
        return "Track<name=%s, tagline=%s, url=%s, desc=%s, director=%s>" % (
            self.name, self.tagline, self.url, self.desc, self.director)


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, db.Sequence('location_id_seq'), primary_key=True)
    room = db.Column(db.String(25))
    building = db.Column(db.String(25))
    note = db.Column(db.String(50))
    events = db.relationship('Event', backref='locations')

    def __repr__(self):
        return "Location<room=%s,building=%s, note=%s>" % (self.room, self.building, self.note)


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, db.Sequence('event_id_seq'), primary_key=True)
    title = db.Column(db.String(100))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    desc = db.Column(db.String(500))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))


if __name__ == '__main__':
    manager.run()