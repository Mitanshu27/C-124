from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'name': u'Ajay Shah',
        'contact':u'7600021127',
        'done':False,
    },
    {
        'id': 2,
        'name': u'Mitanshu Shah',
        'contact': u'9429830555',
        'done':False,
    }
]
@app.route('/add-data',methods=['POST'])
def add_tasks():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'pls provide a data'
        },400)
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'descriptions': request.json.get('descriptions',''),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        'status':'Sucess',
        'message':'task added successfully'
    })
@app.route('/get-data')
def gettasks():
    return jsonify({
        'data':tasks
    })
if(__name__ == '__main__'):
    app.run(debug=True)