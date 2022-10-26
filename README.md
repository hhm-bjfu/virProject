## Flask 练手项目
[教程传送门](https://tutorial.helloflask.com/)

### 程序发现机制
如果你把上面的程序保存成其他的名字，比如 hello.py，接着执行 flask run 命令会返回一个错误提示。这是因为 Flask 默认会假设你把程序存储在名为 app.py 或 wsgi.py 的文件中。如果你使用了其他名称，就要设置系统环境变量 FLASK_APP 来告诉 Flask 你要启动哪个程序：
```cpp
export FLASK_APP = hello.py

```

Flask 通过读取这个环境变量值对应的模块寻找要运行的程序实例，你可以把它设置成下面这些值：

模块名
Python 导入路径
文件目录路径
