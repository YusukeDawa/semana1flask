from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1><b>Hello World!</b></h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1><b>Hello, {name}!</b></h1>'

@app.route('/contextorequisicao')
def contexto():
    return '<p>Your browser is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0</p>'


@app.route('/objetoresposta')
def objeto():
    return '<h1>This document carries a cookie!</h1>'

@app.route('/codigostatusdiferente')
def codigo():
   return '<p>Bad request</p>'


@app.route('/redirecionamento')
def home():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/abortar')
def aborr():
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)