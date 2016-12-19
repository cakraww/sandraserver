from flask import Flask, send_from_directory
import flask
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

@app.route('/photos')
def hello_world():
	FOLDER_PATH = "images"
	photos = [f for f in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, f))]
	return flask.jsonify(photos=photos)

@app.route('/images/<path:path>')
def send_images(path):
	return send_from_directory('images', path)