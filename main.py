from flask import Flask
from flask import request
from multiprocessing import Process
from time import sleep
import sqlite3


app = Flask('SHXNE_SERVER')


@app.route('/new_user')
def new_user():
    try:
        ip = request.args['ip']
        mac = request.args['mac']
        id = request.args['id']
        username = request.args['username']
        name = request.args['name']
        cursor.execute("SELECT * FROM users WHERE ID=?", (id,))
        d = cursor.fetchone()
        if d is None:
            cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", (id, username, name, ip, mac))
        elif d[1] != username and (mac == d[4] or ip == d[3]):
            cursor.execute("UPDATE users SET username=? WHERE id=?", (username, id))
        elif d[2] != name and (mac == d[4] or ip == d[3]):
            cursor.execute("UPDATE users SET name=? WHERE id=?", (name, id))
        elif mac != d[4] or ip != d[3]:
            cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)", (id, username, name, ip, mac))
        con.commit()
        return f'IP -> {ip}|MAC - {mac}'
    except Exception as e:
        print(e)
        return "not_enough_args"
    

@app.route('/task')
def check_task():
    return task


@app.route('/get_users')
def get_users():
    password = request.args['password']
    if password != '12345678qwertyuioplkjhgfdsazxcvbnm':
        cursor.execute("SELECT * FROM users")
        res_data = []
        for user in cursor.fetchall():
            res_data.append({'id': user[0],
                            'username': user[1],
                            'name': user[2],
                            'ip': user[3],
                            'mac': user[4]})
        return str(res_data)
    else:
        return "You don't have access"



@app.route('/add_task')
def add_task():
    global task
    try:
        task = request.args['task']
        password = request.args['password']
        if password != '12345678qwertyuioplkjhgfdsazxcvbnm':
            raise KeyError('dasds')
        if taskkill_xD.is_alive():
            taskkill_xD.kill()
            taskkill_xD.run()
        else:
            taskkill_xD.run()
        return 'Success'
    except:
        return "Not Success"


@app.route('/')
def main():
    return "Server alive!"


def task_proc():
    global task
    sleep(60)
    task = ''

con = sqlite3.connect("users.db", check_same_thread=False, isolation_level=None)
cursor = con.cursor()

task = ''
taskkill_xD = Process(target=task_proc)
app.run("0.0.0.0")
