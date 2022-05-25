from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/', methods = ['GET'])
@app.route('/season/destination', methods = ['GET'])
def get_recommended_holiday():
    season = requests.get('http://service2:5001/get/season').text
    destination = requests.get('http://service3:5002/get/destination').text
    generate = season + ' ' + destination
    review = requests.post ('http://service4:5003/post/review', data = generate).text
    return render_template('home.html', title='Seasonal Holiday Destinations', season=season, destination=destination, review=review)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')

