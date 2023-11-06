import numpy as np
import tensorflow as tf

from difflib import SequenceMatcher
from flask import Flask, render_template, request

model = tf.keras.models.load_model('C:/Users/jpdsn/mini project main/jpd_flask/models/modelop.h5')

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":   
        followers, following, posts, description = [request.form[key] for key in ['followers', 'following', 'posts', 'description']]
        profile_pic, external_url, private = [int(request.form[key] == 'Yes') for key in ['profile_pic', 'external_url', 'private']]
        numslengthusername = float(request.form.get('numslengthusername'))
        fullnamewords = int(len(request.form.get('fullnamewords')))
        numslengthfullname = float(request.form.get('numslengthfullname'))
        useequalfull = int(request.form.get('nameusername'))
        posts, followers, following,description = map(int,(posts, followers, following,description))
        inputs = [profile_pic, numslengthusername, fullnamewords,numslengthfullname,useequalfull, description, external_url, private, posts, followers, following]
        prediction = model.predict(np.array([inputs]))[0][0]
        return f"Prediction: {prediction}"
    return render_template('forms.html')
 
if __name__=='__main__':
   app.run()
 