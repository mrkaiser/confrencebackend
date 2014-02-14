__author__ = 'mrkaiser'

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from migrate import db, app, Person, Event, Track, Location
import os



@app.route('/people/', methods=['GET'])
def people():
    if request.method == 'GET':
        results = Person.query.all()

        json_results = []
        for result in results:
            json_results.append(result.to_json())

        return jsonify(items=json_results)


@app.route('/events/', methods=['GET'])
def events():
    if request.method == 'GET':
        results = Event.query.all()

        json_results = []
        for result in results:
            json_results.append(result.to_json())

        return jsonify(items=json_results)


@app.route('/tracks/', methods=['GET'])
def tracks():
    if request.method == 'GET':
        results = Track.query.all()

        json_results = []
        for result in results:
            json_results.append(result.to_json())

        return jsonify(items=json_results)


@app.route('/locations/', methods=['GET'])
def locations():
    if request.method == 'GET':
        results = Location.query.all()

        json_results = []
        for result in results:
            json_results.append(result.to_json())

        return jsonify(items=json_results)



if __name__ == '__main__':
  app.run(debug=True)