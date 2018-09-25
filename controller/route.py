# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, render_template
import model.mysql as mysql
import json

def toJson(**kwargs):
    return json.dumps(kwargs)  # 把json转换成字符串

app = Flask('mycar')

# url_for('static', filename='style.css')

@app.route('/')
def index():
    return 'who are u ?'

# 管理者端
@app.route('/admin/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:

        username = request.form.get('username')
        password = request.form.get('password')

        connect = mysql.get_conn()
        cursor = connect.cursor()
        mysql.select(cursor, "select * from user where username='%s' and password='%s'" % (username, password))

        if cursor.rowcount > 0:
            # record是一个元组
            print('cursor.rowcount: %s' % cursor.rowcount)
            record = cursor.fetchone()
            for x in record:
                print('record: %s' % x)

            return render_template('admin/map.html', message='登录成功')
        else:
            return render_template('tips.html', message='登录失败：用户名或密码错误！')

# 获取定位数据
@app.route('/api/get-location', methods=['GET', 'POST'])
def getLocation():
    if request.method == 'POST':
        car_id = request.form.get('car_id')
        # token = request.form['token']
        print('car_id: ---------- %s' % car_id)
        connect = mysql.get_conn()
        cursor = connect.cursor()
        mysql.select(
            cursor, '''SELECT lng, lat, create_time, ABS(NOW() - create_time)  AS diff_time 
            FROM location
            where car_id=%d
            ORDER BY diff_time DESC
            LIMIT 0, 1
            ''' % int(car_id))

        if cursor.rowcount > 0:
            # record是一个元组
            # print('cursor.rowcount: %s' % cursor.rowcount)
            record = cursor.fetchone()
            data = [];
            location = {
                'lng': record[0],
                'lat': record[1],
                'create_time': str(record[2])
            }
            data.append(location)
            for x in record:
                print('record: %s' % x)

            return json.dumps({'code': 200, 'data': data})
        else:
            return json.dumps({'code': '200', 'message': '没有数据'})

        print('request: %s ' % request.form)
    return False

# 保存车辆的gps信息
@app.route('/api/save-location/')
def saveLocation(parameter_list):
    return False
