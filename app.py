from flask import Flask # 从flask包中导入Flask类

app = Flask(__name__) # 实例化这个类，参数是当前运行的程序

@app.route('/home') # 使用route装饰器hello函数绑定url，当访问该url时触发函数，并将返回值显示在浏览器窗口

@app.route('/') # 绑定多个url
@app.route('/index')

# 整个请求的处理过程如下所示：
# 1. 当用户在浏览器地址栏访问这个地址，在这里即 http://localhost:5000/
# 2. 服务器解析请求，发现请求 URL 匹配的 URL 规则是 /，因此调用对应的处理函数 hello()
# 3. 获取 hello() 函数的返回值，处理后返回给客户端（浏览器）
# 4. 浏览器接受响应，将其显示在窗口上

def hello():
    return '<h1>Hello hhm!</h1><img src="http://helloflask.com/totoro.gif">'
