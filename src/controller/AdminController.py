from .BaseController import BaseController

class index(BaseController):

    def get(self, requests):
        return self.text("This is admin module.")
