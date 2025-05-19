from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import csv

from io import BytesIO
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

model = load_model("my_food_model.keras")  # <-- make sure this file is in the same folder

class_names = ['apple banana pie', 'biriyani', 'butternaan', 'carrot cake', 'chaat', 'chapati', 'chicken curry', 'chocolate cake', 
               'cupcake', 'dhokla', 'donuts', 'dosa', 'french fries', 'fried rice', 'garlic bread', 'grilled cheese sandwich', 
               'gulab jamun', 'halwa', 'hot dog', 'ice cream', 'idli', 'lobster roll sandwich', 'medu vada',
                'noodles', 'omelette', 'onion rings', 'pancake', 'pizza', 'poori', 'red velvet cake', 'samosa', 'spring roll', 
                'strawberry shortcake', 'tandoori chicken', 'upma', 'vada pav', 'waffles']  # <- just a guess

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/food')
def get_foods():
    food_list = []
    with open('static/data/food.csv', newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            food_list.append(row)
    return jsonify(food_list)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

    # Convert file to BytesIO stream
    img_bytes = BytesIO(file.read())

    # Pass BytesIO stream to load_img
    img = image.load_img(img_bytes, target_size=(224, 224))

    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_label = class_names[predicted_index]

    return jsonify({'prediction': predicted_label})

if __name__ == '__main__':
    app.run(debug=True)
