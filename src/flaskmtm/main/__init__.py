from flask import Blueprint


bp = Blueprint("main", __name__)


from flaskmtm.main import routes
