import os
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from database import db

# -------------------- APP SETUP --------------------
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(base_dir, 'static'),
    static_url_path='/static'
)

CORS(app, resources={r"/*": {"origins": "*"}})

# -------------------- DATABASE CONFIG --------------------
# IMPORTANT: hostname = db (docker-compose mysql service name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vidhi@4104@db:3306/realestate_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize database
db.init_app(app)

# import models AFTER db init
from models import Properties

# -------------------- ROUTES --------------------

@app.route('/')
def home():
    return "Backend Connected Successfully"

# serve images
@app.route('/static/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(base_dir, 'static/images'), filename)

# properties API
@app.route('/api/properties')
def get_properties():
    try:
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------- RUN SERVER --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)