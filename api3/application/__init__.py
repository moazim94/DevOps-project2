from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/destination', methods=['GET'])
def get_destination():
    destination = ['Austria', 'Indonesia', 'India', 'U.A.E']
    randomnum = random.randint(0, 3)
    return Response(destination[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')