from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

with open('students.json', 'r') as file:
    data = json.load(file)


@app.route('/test')
def get_json_data():
    return jsonify(data)

@app.route('/get_student/<id>')
def get_student_details(id):
    with open('students1.json', 'r') as file:
        data = json.load(file)
        
    v = [item for item in data if item["id"] == int(id)]
    return jsonify(v)

@app.route('/post_student/', methods=['POST'])
def post_student_details():
    data1 = request.json
    
    data.append(data1)

    with open('students1.json', 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
