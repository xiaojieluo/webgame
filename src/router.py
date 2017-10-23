from sanic import Blueprint

from controller import IndexController as Index
from controller import APIController as API
from controller import AdminController as Admin


# 定义蓝图
admin = Blueprint('admin', url_prefix = '/admin')
main = Blueprint('main', url_prefix = '/')
api_v1 = Blueprint('api_v1', url_prefix = '/v1')

# main blueprint
Router = [
    (r'/', Index.index, main),
]


# admin blueprint
Router += [
    (r'/',  Admin.index,    admin),
]


# api blueprint
Router += [
    (r'/',  API.index,  api_v1 ),
    # (r'/world', Index.test, api_v1),
]
