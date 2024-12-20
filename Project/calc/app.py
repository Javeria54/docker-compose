from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return jsonify(result=a + b), 200
    return 'Invalid input', 400

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return jsonify(result=a - b), 200
    return 'Invalid input', 400

@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return jsonify(result=a * b), 200
    return 'Invalid input', 400

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        if b == 0:
            return 'Division by zero', 400
        return jsonify(result=a / b), 200
    return 'Invalid input', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
