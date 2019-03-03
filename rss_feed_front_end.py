import os
from flask import Flask, render_template, request, json, jsonify

# Initialize flask object
app = Flask(__name__)

# This route is used for the main page of the tool
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/v1/get-articles', methods=['GET'])
def get_articles():
	# number_articles = request.args.get('number').lower()
	# start_key = request.args.get('start')
	# print(number_articles)
	# print(start_key)

	# Read dummy static JSON for response temporarily
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/", "sample.json")
	data = json.load(open(json_url))
	return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)