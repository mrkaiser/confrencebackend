__author__ = 'mrkaiser'

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from migrate import db, Person, Event, Track, Location
import os

app = Flask(__name__)


@app.route('/people/', methods=['GET'])
def people():
    if request.method == 'GET':
        results = Person.query.limit(10).all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'first_name': result.first_name,
                 'last_name': result.last_name,
                 'url': result.url,
                 'about': result.about}
            json_results.append(d)

        return jsonify(items=json_results)


@app.route('/events/', methods=['GET'])
def events():
    if request.method == 'GET':
        results = Event.query.all()

        json_results = []
        for result in results:
            d = {'id': result.id,
                 'title': result.title,
                 'location': result.location_id,
                 'desc': result.desc,
                 'track': result.track_id}
            json_results.append(d)

        return jsonify(items=json_results)



if __name__ == '__main__':
  app.run(debug=True)