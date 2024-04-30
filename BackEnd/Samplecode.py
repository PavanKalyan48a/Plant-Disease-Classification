from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define a route for the root endpoint
@app.route('/')
def hello():
    return 'Hello, this is your Flask backend!'

# Define a route for a custom endpoint that returns JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'This is sample data from the backend API',
        'status': 'success'
    }
    return jsonify(data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
