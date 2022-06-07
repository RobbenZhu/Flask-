from flask import Flask
# 对Flask重命名
app = Flask(__name__)

# 创建请求响应函数
# 用装饰器来装饰路由
@app.route('/index')
def index():
    return 'Hello World'


if __name__ == '__main__':
    # 运行Flask
    app.run()


