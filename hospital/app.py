from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from flask import jsonify
app = Flask(__name__, static_folder='templates/static' , template_folder='templates/')

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/predict', methods=['POST','GET'])
def predict():
    data = request.json['data']
    print('Data received:', data)  # Add this print statement

    # Preprocess the data if necessary
    # Perform any required feature engineering, scaling, etc.

    # Make predictions using the loaded model
    predictions = model.predict([data])

    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions.tolist()})
if __name__ == '__main__':
    app.run()
