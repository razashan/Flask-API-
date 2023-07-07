from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['POST'])
def calculate_square():
    data = request.get_json()
    number = data.get('number')
    if number is None:
        return jsonify({'error': 'Number is required'}), 400
    
    try:
        number = float(number)
    except ValueError:
        return jsonify({'error': 'Invalid number'}), 400
    
    square = number * number
    return jsonify({'result': square})

if __name__ == '__main__':
    app.run(debug=True)
