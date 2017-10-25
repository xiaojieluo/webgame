from .BaseController import BaseController


class index(BaseController):

    def get(self, requests):
        # template = "<b>[游戏设计大厅]</b>"
        return self.render('admin/index.html')
        # return self.html(template)
        # return self.text("This is admin module.")
