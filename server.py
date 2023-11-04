from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b!=0:
        return a/b
    else:
        return "Cannot divide by zero"

@app.route('/rpc', methods=['POST'])
def rpc():
    data = request.get_json()
    method = data.get('method')
    params = data.get('params')

    if method == 'add':
        result = add(*params)
        return jsonify({'result': result})
    elif method == 'subtract':
        result = subtract(*params)
        return jsonify({'result': result})
    elif method == 'multiply':
        result = multiply(*params)
        return jsonify({'result': result})
    elif method == 'divide':
        result = divide(*params)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Method not found'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)