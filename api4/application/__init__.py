from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/review', methods=['POST'])
def post_review():
    generate = request.data.decode('utf-8')
    final_task = generate.split(' ')
    if final_task[1] == 'Indonesia' and final_task[0] == 'Spring-(Mar-May)':
        review = 'Avoid Indonesia in the first month of spring as it is the end of monsoon season. April begins the dry season months.'
    elif final_task[1] == 'Indonesia' and final_task[0] == 'Summer-(Jun-Aug)':
        review = 'Indonesia is now dry and sunny, making it the perfect time to hit popular places like Bali, East Java, Komodo.'
    elif final_task[1] == 'Indonesia' and final_task[0] == 'Autumn-(Sep-Nov)':
        review = 'September and October months round up the end of the Indonesian dry season and the Island nation gets prepared for the start of monsoon season in November.'
    elif final_task[1] == 'Indonesia' and final_task[0] == 'Winter-(Dec-Feb)':
        review = 'Indonesia begins and remains in monsoon season until April, not reccomended destination at this time'
    elif final_task[1] == 'Austria' and final_task[0] == 'Spring-(Mar-May)':
        review = 'The Austrian Alps come to life in the springtime, with wildflowers, green meadows, and dramatic mountains views.'
    elif final_task[1] == 'Austria' and final_task[0] == 'Summer-(Jun-Aug)':
        review =  'June-Aug bring beautiful summer weather, particularly the further south you go. Of course the high mountains are always cooler, but with risks of lightning in summer.'
    elif final_task[1] == 'Austria' and final_task[0] == 'Autumn-(Sep-Nov)':
        review = 'Autumn is an excellent time to visit Austria. You can partake in jubilant harvest festivals, see an Almabtrieb cattle procession, drink Sturm (early wine) in cosy Heurigen (wine taverns).'
    elif final_task[1] == 'Austria' and final_task[0] ==  'Winter-(Dec-Feb)':
        review = 'Christmas and New Year in Austria are magically festive, with gluhwein and Christmas markets everywhere you go, no matter how remote.'
    elif final_task[1] == 'India' and final_task[0] == 'Spring-(Mar-May)':
        review = 'India is one of the best countries to visit in March, especially if you want to participate in their colorful Holi Festival.'
    elif final_task[1] == 'India' and final_task[0] == 'Summer-(Jun-Aug)':
        review = 'India, is still in their monsoon season, a good time to avoid as a holiday destination'
    elif final_task[1] == 'India' and final_task[0] == 'Autumn-(Sep-Nov)':
        review = 'India has finally come out of its long monsoon season. September brings pleasant weather which makes it a good month to visit the country before the winter crowds come.'
    elif final_task[1] == 'India' and final_task[0] == 'Winter-(Dec-Feb)':
        review = 'A winter holiday in India is one of the best experiences one can have. Indulge in skiing, beach fun, water sports, relaxing, festivals, wildlife adventure and other delightful experiences during winters in India.'
    elif final_task[1] == 'U.A.E' and final_task[0] == 'Spring-(Mar-May)':
        review = 'During this time of year, there is a perfect balance as the days are starting to become hotter and last longer, while nighttime temperatures are dropping so be sure to take along a light jacket for the evening.'
    elif final_task[1] == 'U.A.E' and final_task[0] == 'Summer-(Jun-Aug)':
        review = 'Dubai will experience an average of 10-12 hours of daylight and will need to seek shade during the main part of the day, when temperatures are extremely hot, best to avoid if not use to extreme temperatures.'
    elif final_task[1] == 'U.A.E' and final_task[0] == 'Autumn-(Sep-Nov)':
        review = 'during these months, you can bask in the warmth of the United Arab Emirates desert-like climate and avoid the peak of the heat.'
    elif final_task[1] == 'U.A.E' and final_task[0] == 'Winter-(Dec-Feb)':
        review = 'The coolest month of the year for Dubai is January, where the average daytime high is 24 degrees. The average overnight low in January is 14 degrees and the average sea temperature of Dubai in January is 23 degrees. A perfect sunny Christmas break.'
    else:
        review = 'Wild Card destination'

    return Response(review, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')