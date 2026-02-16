import os

from flask import Flask, jsonify
from flask_cors import CORS
from database import db

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_folder=os.path.join(base_dir, 'static'), static_url_path='/static')


CORS(app)

# MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vidhi%404104@127.0.0.1:3306/realestate_db'

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
            "image_url": f"http://127.0.0.1:5000{p.image_url}"
        })

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)
