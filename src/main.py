from sanic import Sanic
from BeautifulDebug import dump, setting
from sanic import Blueprint
from colorama import Fore

from router import Router

def make_app():
    app = Sanic(__name__)
    # 蓝图列表
    bps = []
    # 解析路由
    for url, value, bp in Router:
        bp.add_route(value.as_view(), url)
        if bp not in bps:
            bps.append(bp)

# 这里 app.blueprint(bp) 不能放在上面的循环中，
# 因为如果如果没有循环完路由表就注册了蓝图， 那么后面的路由就不会加载到系统中，程序会报错。
    for bp in bps:
        print(Fore.YELLOW + "Loading blueprint {} :\t{}".format(bp.name, bp))
        for item in bp.routes:
            print(Fore.CYAN + "\t{}".format(item))
        app.blueprint(bp)
    print(app.blueprints)

    # 启动服务器
    app.run(host = "0.0.0.0",
            port = 8000,
            debug = True)

if __name__ == '__main__':
    make_app()
