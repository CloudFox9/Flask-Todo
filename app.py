from flask import Flask, request, Response
import json
from database import * #database
from constants import * #some constants for easy coding
app = Flask(__name__)



@app.route('/')
def todoApplication():
    return 'Todo List Application Backend API'

#addition of new task
@app.route('/task/add', methods=['POST'])
def addTask():
    try:
        task = request.form['task']
        if task:
            res = addTask(task)
        else:
            res = InvalidRequest
    except Exception as e:
            res = errorFunction(e)
    response = Response(json.dumps(res), mimetype='application/json')
    return response


#edit existing task details
@app.route('/task/edit', methods=['POST'])
def editTask():
    try:
        task = request.form['newtask']
        id = request.form['id']
        if task and id:
            res = editTaskDB(task,id)
        else:
            res = InvalidRequest
    except Exception as e:
            res = errorFunction(e)
    response = Response(json.dumps(res), mimetype='application/json')
    return response

#remove a task from list
@app.route('/task/delete', methods=['POST'])
def delTask():
    try:
        id = request.form['id']
        if  id:
            res = delTaskDB(id)
        else:
            res = InvalidRequest
    except Exception as e:
            res = errorFunction(e)
    print(res)
    response = Response(json.dumps(res), mimetype='application/json')
    return response

#all tasks
@app.route('/task/all', methods=['GET'])
def getTask():
    try:
        res = {"tasks" : getTaskDB()}
    except Exception as e:
            res = errorFunction(e)
    print(res)
    response = Response(json.dumps(res), mimetype='application/json')
    return response


#change task status
@app.route('/task/mark', methods=['POST'])
def markTask():
    try:
        id = request.form['id']
        if  id:
            res = markTaskDB(id)
        else:
            res = InvalidRequest
    except Exception as e:
            res = errorFunction(e)
    print(res)
    response = Response(json.dumps(res), mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run()