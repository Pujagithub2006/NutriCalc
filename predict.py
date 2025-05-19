import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tkinter import Tk, filedialog





import webbrowser
import urllib.parse




# Load the model you uploaded
model = load_model(r"C:\Users\91901\OneDrive\Desktop\my_food_model.keras")

# ⛔ IMPORTANT: Replace these with actual class names used during training
class_names = ['apple pie', 'biriyani', 'butternaan', 'carrot cake', 'chaat', 'chappati', 'chicken curry', 'chocolate cake', 
               'cup cakes', 'dhokla', 'donuts', 'dosa', 'french fries', 'fried rice', 'garlic bread', 'grilled cheese sandwich', 
               'gulab jamun', 'halwa', 'hot dog', 'ice cream', 'idly', 'lobster roll sandwich', 'meduvadai',
                'noodles', 'omelette', 'onion rings', 'pancakes', 'pizza', 'poori', 'red velvet cake', 'samosa', 'spring rolls', 
                'strawberry shortcake', 'tandoori chicken', 'upma', 'vada pav', 'waffles']  # <- just a guess

# Function to load an image and predict its class
def predict_food(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Change if model used a different size
    img_array = image.img_to_array(img) / 255.0  # Normalization
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_label = class_names[predicted_index]

    print(f"Predicted Food Item: {predicted_label}")




    encoded_label = urllib.parse.quote(predicted_label)
    url = f"http://localhost:5500/index.html?query={encoded_label}"
    webbrowser.open(url)



    

# Function to open file dialog and select an image
def select_file_and_predict():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )

    # Check if a file was selected
    if file_path:
        print(f"Selected File: {file_path}")
        predict_food(file_path)
    else:
        print("No file selected.")

# Call the function to open file dialog and predict
select_file_and_predict()