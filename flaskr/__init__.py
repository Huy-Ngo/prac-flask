""" REST API with flask
This is an exercise to build a REST API with flask (get, post, put, delete)
Based on https://flask.palletsprojects.com/en/1.1.x/tutorial/
"""
import os
from flask import Flask

def create_app(test_config=None):
	"""Test and configure the app"""
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev', # to keep data safe, conv used for development, should be a random value when deploying
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)

	if test_config is None:
		# load the instance config, if it exists, while not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# a simple page that says Hello
	@app.route('/hello')
	def hello():
		return 'Hello bitch'

	from . import db
	db.init_app(app)

	return app