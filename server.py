__author__ = 'mrkaiser'

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
                                                       "mysql+mysqlconnector://username:password@localhost/database")

from models import Event, Location, Person, Track

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


if __name__ == '__main__':
  app.run(debug=True)