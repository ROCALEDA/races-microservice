from flask import Blueprint

races_bp = Blueprint('races', __name__)


@races_bp.get("/ping")
def ping():
    return "pong"
