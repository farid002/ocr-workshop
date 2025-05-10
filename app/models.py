from . import db

class OCRData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200))
    text = db.Column(db.Text)
    summary = db.Column(db.Text)
    translation = db.Column(db.Text)
    audio_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
