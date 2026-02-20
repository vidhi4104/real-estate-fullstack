import os
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify
from flask_cors import CORS
from database import db

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_folder=os.path.join(base_dir, 'static'), static_url_path='/static')
from flask import send_from_directory

@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(base_dir, 'static/images'), filename)


CORS(app, resources={r"/*": {"origins": "*"}})


# MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql:3306/realestate_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




# initialize database
db.init_app(app)

# import models AFTER db init
from models import Properties

@app.route('/')
def home():
    return "Backend Connected Successfully"

@app.route('/api/properties')
def get_properties():
    properties = Properties.query.all()

    result = []
    for p in properties:
        result.append({
            "id": p.id,
            "title": p.title,
            "location": p.location,
            "price": p.price,
            "type": p.type,
            "status": p.status,
            "description": p.description,
            "image_url": p.image_url


        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

