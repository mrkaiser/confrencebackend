__author__ = 'mrkaiser'

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from migrate import db, app, Person, Event, Track, Location
import os


def results_to_json(results):
    json_results = []
    for result in results:
        json_results.append(result.to_json())
    return jsonify(items=json_results)


@app.route('/people/', methods=['GET'])
def people():
    if request.method == 'GET':
        results = Person.query.all()

        return results_to_json(results)


@app.route('/people/<int:person_id>', methods=['GET'])
def person_by_id(person_id):
    results = Person.query.filter(Person.id == person_id).all()

    return results_to_json(results)


@app.route('/events/', methods=['GET'])
def events():
    if request.method == 'GET':
        results = Event.query.all()

        return results_to_json(results)


@app.route('/events/<int:event_id>', methods=['GET'])
def event_by_id(event_id):
    results = Event.query.filter(Event.id == event_id).all()

    return results_to_json(results)


@app.route('/tracks/', methods=['GET'])
def tracks():
    if request.method == 'GET':
        results = Track.query.all()

        return results_to_json(results)


@app.route('/tracks/<int:track_id>', methods=['GET'])
def track_by_id(track_id):
    results = Track.query.filter(Track.id == track_id).all()

    return results_to_json(results)


@app.route('/locations/', methods=['GET'])
def locations():
    if request.method == 'GET':
        results = Location.query.all()

        return results_to_json(results)


@app.route('/locations/<int:location_id>', methods=['GET'])
def location_by_id(location_id):
    results = Location.query.filter(Location.id == location_id).all()

    return results_to_json(results)


if __name__ == '__main__':
    app.run(debug=True)