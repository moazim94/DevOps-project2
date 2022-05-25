from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/get/season', methods = ['GET'])
def get_season():
    season = ['Spring-(Mar-May)', 'Summer-(Jun-Aug)', 'Autumn-(Sep-Nov)', 'Winter-(Dec-Feb)']
    randomnum = random.randint(0, 3)
    return Response(season[randomnum], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port = 5001, debug = True, host = '0.0.0.0')

