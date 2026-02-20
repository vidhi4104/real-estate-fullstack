from database import db

class Properties(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    location = db.Column(db.String(150))
    price = db.Column(db.Integer)
    type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
