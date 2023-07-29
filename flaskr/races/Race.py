from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flaskr import db


class Race(db.Model):
    __tablename__ = "carrera"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String)
    estaTerminada = db.Column(db.Boolean)


class RaceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Race
        load_instance = True


races_schema = RaceSchema(many=True)
