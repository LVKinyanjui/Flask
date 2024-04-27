
from flask import Flask, render_template, request

app = Flask ("My first Application")

@app.route('/')
def index():
    return "Hello World"

@app.route ('/sample')
def getSampIeHtmI():
    return render_template('sample.html')

@app.route('/user/<username>' , methods=['GET'])
def greetUser(username) :
    return render_template( "result.html" , username=username)
