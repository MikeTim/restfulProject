from flask import Flask, render_template, request
import urllib2
import json


MainRestful = Flask(__name__)

@MainRestful.route('/main')
def main():
	#Opens File v
	data1 = urllib2.open('https://api.wheretheiss.at/v1/satellites/25544')
	#print data
	data2 = json.loads(data1)
	#data2 = data.read()
	#data.close
	lat = data2['latitude']
	long = data2['longitude']
	location = str(lat + " " + long)
	return location


@MainRestful.route('/result')
def result():
	return render_template("index.html")

#DEBUGGING PAGE !!!( TESTING )!!!
@MainRestful.route('/testing')
def testpage():
	return location




if __name__ == '__main__':
	MainRestful.run()
	MainRestful.debug = True
