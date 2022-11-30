from flask import Flask, jsonify
from datetime import datetime
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

arr = {'time': str(datetime.now().time()), 'voltage': random.randrange(1650, 1700)}
print(arr)

# route for voltage. This will return a json with the format {"time":"22:08:25.379760","voltage":1685}
@app.route('/voltage')
def voltage() :
    arr = {'time': str(datetime.now().time()), 'voltage': random.randrange(1650, 1700)}
    return(jsonify(arr))
    

# this one will return an array of 250 voltages instead of one voltage
# route for voltage array. This will return a json with an array of 250 voltage samples with the format {"time":"22:08:25.379760","voltage":1685}
@app.route('/voltage2')
def voltage2() :
    arr = {"data": [{'time': str(datetime.now().time()), 'voltage': random.randrange(1650, 1700)}]}
    for i in range(250):
        arr['data'].append({'time': str(datetime.now().time()), 'voltage': random.randrange(1650, 1700)})
    return jsonify(arr)

if __name__ == '__main__':
    app.run(port=5005)