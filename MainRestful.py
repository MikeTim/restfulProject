from flask import Flask, render_template, request
import urllib
#!/usr/bin/python

MainRestful = Flask(__name__)

@MainRestful.route('/')
def main():
	data = urllib.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
	data2 = data.read()
	data.close
	return data2	
	lat = data2['latitude']
	long = data2['longitude']
	location = lat + " " + long
	#return json.loads(data)
	return location
	
if __name__ == '__main__':
	MainRestful.run()
	MainRestful.debug = True
