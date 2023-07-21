import requests
from tensorflow.keras.preprocessing import Image
from tonsorflow.keras.models import load_model
import numpy as np 
import pandas as pd 
import tensorflow as tf
from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.python.keras.backend import set_session
app=Flask(__name__)
model=load_model("vegetable.h5")
model=load_model("fruit.h5")
#home page
@app.route('/')
def home ():
    return render_template('home.html')
@app.route('/')
def prediction ():
    return render_template('prediction.html')
    #prediction page
@app.route('/predict', methods=['POST'])
def predict():
if request.method == 'POST':
#Get the file from post request
f= request.files['image']
#Save the file to ./uploads
basepath = os.path.dirname(__file__)
file_path = os.path.join(
basepath, 'uploads', secure_filename (f.filename))
f.save(file_path)
img = image.load_img(file_path, target_size=(128, 128)) 
x = image.img_to array(img)
X = np.expand_dims (x, axis=0)
plant-request.form['plant']
print (plant)
if (plant=="vegetable"):
preds = model.predict_classes (x)
print (preds)
df=pd.read_excel ('precautions- veg.xlsx') 
print (df.iloc[preds[0]]['caution'])
else:
    preds = modell.predict_classes (x)
df=pd.read_excel ('precautions - fruits.xlsx")
print (dr.iloc[preds[0]]['caution'])
return df.iloc[preds[0]]['caution']
if __name__ == "__main__":
    app.run(debug=False)








