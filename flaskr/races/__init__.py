from flask import Blueprint, Flask

from flaskr.races.RaceRepository import RaceRepository
from flaskr.races.Race import races_schema

races_bp = Blueprint('races', __name__)
races_repository = None


class RacesViews:
    def __init__(self, app: Flask) -> None:
        global races_repository
        app.register_blueprint(races_bp, url_prefix='/races')
        races_repository = RaceRepository()

    @staticmethod
    @races_bp.get("/ping")
    def ping() -> None:
        return "pong"

    @staticmethod
    @races_bp.get("/")
    def get_races():
        races = races_schema.dump(races_repository.get_all())
        return races, 200

    @staticmethod
    @races_bp.get("/<id>")
    def get_race_by_id(id: int):
        race = races_repository.get_by_id(id)
        
        if race is not None:
            return {"id": race.id, "nombre": race.nombre, "estaTerminada": race.estaTerminada}, 200

        return "Race not found", 404
