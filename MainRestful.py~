from flask import Flask, render_template, request
import urllib2
import json


MainRestful = Flask(__name__)

@MainRestful.route('/main')
def main():
	#Opens File v
	data1 = urllib2.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
	data2 = data1.read()
	data3 = json.loads(data2)
	print " one"
	print data3
	print "two"
	lat = data3['latitude']
	print lat
	long = data3['longitude']
	print long
	location = str(lat) + " " + str(long)
	print location
	#return "DEBUG TEXT"
	data1.close()
	return render_template("index.html", location = location)





@MainRestful.route('/result')
def result():
	return render_template("index.html")

#DEBUGGING PAGE !!!( TESTING )!!!
@MainRestful.route('/testing')
def testpage():
	data1 = urllib2.open('https://api.wheretheiss.at/v1/satellites/25544')
	print data1
	data2 = json.loads(data1)
	print data2




if __name__ == '__main__':
	MainRestful.run()
	MainRestful.debug = True
