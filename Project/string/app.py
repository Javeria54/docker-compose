from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upper')
def upper():
    text = request.args.get('text', type=str)
    if text:
        return jsonify(result=text.upper()), 200
    return 'Invalid input', 400

@app.route('/lower')
def lower():
    text = request.args.get('text', type=str)
    if text:
        return jsonify(result=text.lower()), 200
    return 'Invalid input', 400

@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a and b:
        return jsonify(result=a + b), 200
    return 'Invalid input', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
