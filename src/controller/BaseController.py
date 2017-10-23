from sanic.views import HTTPMethodView
from sanic.response import json, text

class BaseController(HTTPMethodView):

    def __init__(self):
        self.json = json
        self.text = text
