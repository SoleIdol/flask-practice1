# author:Administrator
# filename: manage.py
# datetime:2020/8/17 14:32
"""
带参数的路由练习
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu/')
def menu():
    # menu = ['红烧肉', '鱼香肉丝', '尖椒鸡蛋', '宫保鸡丁', '大盘鸡']
    menu = []
    return render_template('for_test1.html', menu=menu)


@app.route('/login/', methods=('POST', 'GET'))
def login():
    return render_template('login.html')


@app.route('/main/', methods=('POST', 'GET'))
def main():
    print('方式为：', request.method)
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
    else:
        name = request.args.get('name')
        passwd = request.args.get('passwd')
    return render_template('main.html', name=name, passwd=passwd)


@app.route('/method/<mot>/<int:a>_<int:b>')
def add(mot, a, b):
    if mot == 'add':
        result = a + b
        fh = '+'
    elif mot == 'sub':
        result = a - b
        fh = '-'
    elif mot == 'mul':
        result = a * b
        fh = '*'
    elif mot == 'div':
        result = a / b
        fh = '/'
    else:
        return 'Unknow'
    return f'{a} {fh} {b} = {result}'


@app.route('/foo1/')
def foo1():
    name = request.args['name']
    age = request.args['age']
    hobby = request.args.get('hobby')
    return f'{name}今年{age}岁了,喜欢{hobby}'


@app.route('/bug/')
def bug():
    a = 12
    b = 0
    return f'a/b={a / b}'


class Stu(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def look(self):
        return f'{self.name}喜欢看漂亮的小姐姐'


stu = Stu('jack', -12)


@app.route('/look/')
def look():
    dic = [{'name': '王昭君', 'age': 23}, {'name': '安琪拉', 'age': 22}, {'name': '大智若愚', 'age': 22},
           {'name': '甄姬', 'age': 24}, {'name': '鲁班七号', 'age': 28}, {'name': '猪八戒', 'age': 23},
           {'name': '不知火舞', 'age': 25}, {'name': '程咬金', 'age': 29}, {'name': '达摩', 'age': 24},
           {'name': '不知好歹', 'age': 25}, {'name': '玄策', 'age': 27}, {'name': '百里守约', 'age': 26}]
    return render_template('test.html', dict=dic, stu=stu)


if __name__ == '__main__':
    print('静态文件硬盘地址：',app.static_folder)  # 静态文件在硬盘上的绝对路径
    print('静态文件url：',app.static_url_path)  # 静态文件在网首页上的url地址
    app.debug = True  # 也可以写在run()中
    app.run(host='127.0.0.1', port='8000')
