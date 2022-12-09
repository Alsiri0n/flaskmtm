import os
from flaskmtm import create_app


app = create_app(os.environ.get("CONFIG"))
