from flask import Flask, jsonify, make_response

app = Flask('docker-python-flask')

@app.route('/', methods=['GET'])
def hello():
    response = {'message': 'It Works!'}
    return make_response(jsonify(response), 200)

@app.route('/<path:path>', methods=['GET', 'POST'])
def not_found(path):
    response = {'error': 'route not found'}
    return make_response(jsonify(response), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
