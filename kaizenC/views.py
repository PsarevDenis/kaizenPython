"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from kaizenC import app

import pymssql

from datetime import datetime

from flask import render_template, request, redirect

server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index():
    return render_template("index.html")

@app.route('/kaizenCommand/<index>/', methods=['POST'])
def kaizenCommand(index):
    if(index == '0'):
        
        connection = pymssql.connect(server="DESKTOP-4JKHTQ3", user="kaizen", password="1q2w3e", database="kaizenCommand")
        cursor = connection.cursor()

        cursor.execute("SELECT [NAME] FROM Department")

        depsAr = cursor.fetchall()
        
        connection.close()

        return render_template("kaizenCommand.html", deps = depsAr)
    if(index == 'p'):
        if request.method == 'POST':
            return render_template("problem.html")

@app.route('/problem/<index>/', methods=['POST'])
def problem(index):
    if(index == '0'):
        
        if request.form['submit'] == 'addCauses':
            connection = pymssql.connect(server="DESKTOP-4JKHTQ3", user="kaizen", password="1q2w3e", database="kaizenCommand")

            cursor = connection.cursor()

            cursor.execute("SELECT [NAME] FROM Classifier")

            classAr = cursor.fetchall()
        
            connection.close()

            return render_template("rootCauses.html", classes = classAr)
        if request.form['submit'] == 'problem':
            return render_template("problem.html")
        if request.form['submit'] == 'saveRootCauses':
            return render_template("problem.html")

    if(index == 'p'):
        if request.method == 'POST':
            return render_template("problem.html")

    if(index == 'rC'):
        if request.form['submit'] == 'findRootCauses':
            return render_template("causesConstructor.html")
        if request.form['submit'] == 'saveRootCaus':
            return render_template("listRootCauses.html")
       
    if(index == 's'):
        return render_template("problem.html")
    
@app.route('/kaizenIdea/<index>/', methods=['POST'])
def kaizenIdea(index):
    if(index == '0'):

        if request.form['submit'] == 'addProblem':
            return render_template("addProblem.html")

        if request.form['submit'] == 'addRootCauses':
            return render_template("listRootCauses.html")

        if request.form['submit'] == 'kaizenIdea':
            return render_template("kaizenIdea.html")
    if(index == 's'):
        return render_template("kaizenIdea.html")

@app.route('/listRootCauses/<index>/', methods=['POST'])
def listRootCauses(index):
    if(index == '0'):
        return render_template("listRootCauses.html")

@app.route('/rootCauses/<index>/', methods=['POST'])
def rootCauses(index):
    if(index == 0):
        return render_template("rootCauses.html")


@app.route('/workWithEvent/<index>/', methods=['POST'])
def workWithEvent(index):
    if(index == '0'):
        return render_template("workWithEvent.html")
    if(index == 'e'):
        if request.form['submit'] == 'addIdea':
            return render_template("addIdea.html")
        if request.form['submit'] == 'kaizenEvent':
            return render_template("workWithEvent.html")
        if request.form['submit'] == 'addEvent':
            return render_template("addEvent.html")
        if request.form['submit'] == 'endCommand':
            return render_template("index.html")
    if(index == 's'):
        return render_template("workWithEvent.html")
        

@app.route('/anysisKk/<index>/', methods=['POST'])
def anysisKk(index):
    if(index == '0'):
        return render_template("anysisKk.html")



