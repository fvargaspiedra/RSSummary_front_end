from flask import Flask, render_template, request

# Initialize flask object
app = Flask(__name__)

# This route is used for the main page of the tool
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/v1/get-all-articles', methods=['GET'])
def get_all_articles():
    return 'Hello World.', 201

if __name__ == '__main__':
    app.run(debug=True)
