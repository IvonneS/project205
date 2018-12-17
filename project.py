
import pyowm

from flask import Flask, render_template,request,redirect, url_for
from flask_bootstrap import Bootstrap
from pprint import pprint
from PIL import Image
import requests, json, urllib
import pygal



api_address= 'http://api.openweathermap.org/data/2.5/weather?appid=5255697ebf72d8fd089e9dcffef16da9&q='
city = input("City Name :")
url = api_address + city

json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['main']
#print(formatted_data) # test results one word discription


image_info = [
{
"id" : "00",
"title" : "It is currently cloudy! grab a light coat.",
},

{
"id" : "01",
"title" : "It is currently raining! Grab a umbrella.",
},
{
"id" : "02",
"title" : "Its a beautiful clear day! Grab some sunscreen. ",
},
{
"id" : "03",
"title" : "There is currently a thunderstorm! Stay indoors. ",
},

{
"id" : "04",
"title" : "Its currently foggy, Drive with caution. ",
},
{
"id" : "05",
"title" : "Its currently misty!, stay dry. ",
},
]
 #owm = pyowm.OWM('0162282d3b4a251981a565c3ad17ca9f')
    #observation = owm.weather_at_place('London, GB')
    #w = observation.get_weather('london, GB') # w is list
    #return render_template('home2.html', w=w)
app = Flask(__name__)
Bootstrap(app)
@app.route('/home', methods=['GET','POST'])
def homepage():
    name = " "
    title = " "
    degrees = " "
    for x in formatted_data:
        if x == "C":
            name = image_info[0]['id']
            title = image_info[0]['title']
            degrees = "57 °F"
        elif x == "R":
            name = image_info[1]['id']
            title = image_info[1]['title']
            degrees = "55 °F"
        elif x == "Cl":
            name = image_info[2]['id']
            title = image_info[2]['title']
            degrees = "70 °F"
        elif x == "T":
            name = image_info[3]['id']
            title = image_info[3]['title']
            degrees = "50 °F"
        elif x == "F":
            name = image_info[4]['id']
            title = image_info[4]['title']
            degrees = "57 °F"
        elif x == "M":
            name = image_info[5]['id']
            title = image_info[5]['title']
            degrees = "60 °F"

        return render_template('home.html', name = name +".jpg",title = title, degrees = degrees)

@app.route('/info')
def pygalgraph():
    try:
        line_chart = pygal.Line()
        line_chart.title = 'Monterey Climate Graph - California 2018'
        line_chart.x_labels = map(str, range(1, 13))
        line_chart.add('High in °F', [58, 60, 61, 62, 63, 65, 66, 68, 70, 68, 63, 58])
        line_chart.add('Low in °F',  [44, 45, 45, 46, 48, 50, 52, 53, 53, 51, 47, 44])

        return line_chart.render_response()
    except ErrorValue:
        print("Oops! Try again...")

@app.route('/about')
def a():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True  # Uncomment to enable debugging
    app.run() # run server
#**********************************
