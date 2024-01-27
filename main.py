from bottle import *
import sqlite3

@route('/test')
def testFunction():
    return template('index.html')

@post('/test')
def postFunction():
    return "<p> bottle X Htmx 4 life</b>"

run(host='0.0.0.0',port=8000,reloader=True)

