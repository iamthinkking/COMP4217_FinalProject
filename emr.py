from flask import Flask, request, redirect, render_template, url_for
import dataconnector


app = Flask(__name__)

app.config['SQL_HOST'] = 'localhost'
app.config['SQL_CRED'] = {}
app.config['SQL_DB'] = 'HOSPITAL'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        app.config.update(
            SQL_CRED=dict(USR=request.form['username'],
                          PWD=request.form['password'])
        )
        print(app.config['SQL_CRED'])
        if app.config['SQL_CRED']['USR'] == '' or app.config['SQL_CRED']['PWD'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            with dataconnector.Connection(app.config['SQL_CRED']['USR'], app.config['SQL_CRED']['USR']) as con:
                usr = con.login()
                return render_template('home.html', username=usr)
    return render_template('login.html', error=error)


@app.route('/home/<username>', methods=['GET', 'POST'])
def home(usr):
    x = 0
