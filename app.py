# 
from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world hehe world'

# 管理者端
@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('tips.html', message='登录成功')

@app.route('/admin/map')
def map():
    return render_template('map.html')


@app.route('/client/location')
def clientLocation():
    return render_template('client.html')

# 保存车辆的gps信息
@app.route('/api/save-location/')
def saveLocation(parameter_list):
    return False

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    # app.run(debug=True)
