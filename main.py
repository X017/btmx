from bottle import *
import sqlite3

@route('/test')
def testFunction():
    return template('test.tpl')

@post('/test')
def postFunction():
    return "<p> Hello World</b>"

run(host='0.0.0.0',port=8000,reloader=True)