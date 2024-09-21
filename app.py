from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define an API endpoint
@app.route('/api/data', methods=['POST'])
def get_data():
    # Get data from the request
    data = request.json
    # Process the data (example: just return it)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)