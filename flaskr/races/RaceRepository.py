from sqlalchemy import asc
from flaskr.races.IRaceRepository import IRaceRepository
from flaskr.races.Race import Race


class RaceRepository(IRaceRepository):
    def get_by_id(self, id: int):
        return Race.query.filter_by(id=id).first()

    def get_all(self):
        return Race.query.order_by(asc(Race.name)).all()
