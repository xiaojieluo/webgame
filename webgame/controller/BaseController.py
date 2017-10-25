from sanic.views import HTTPMethodView
from sanic.response import json, text, html
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os

class BaseController(HTTPMethodView):

    def __init__(self):
        self.json = json
        self.text = text
        self.html = html
        self.env = Environment(
            variable_start_string = '{',
            variable_end_string = '}',
            loader = PackageLoader('webgame', 'templates'),
            autoescape = select_autoescape(['html', 'xml'])
        )
        self.setting = {
            'template_dir': 'views'
        }

    def render(self, filename, **kw):
        '''渲染文件模板'''
        # filename = os.path.join(self.setting['template_dir'], filename)
        # print(filename)
        print(self.env.list_templates())
        template = self.env.get_template(filename)
        render = template.render(**kw)
        return self.html(render)

    def render_string(self, string, **kw):
        '''渲染字符串模板'''
        render = self.env.from_string(string).render(**kw)
        return self.html(render)
