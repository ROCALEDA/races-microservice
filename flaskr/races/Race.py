from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flaskr import db


class Race(db.Model):
    __tablename__ = "race"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    isFinished = db.Column(db.Boolean)


class RaceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Race
        load_instance = True


races_schema = RaceSchema(many=True)
