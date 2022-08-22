from joblib import load
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import re
import string
from sklearn.feature_extraction import _stop_words
stopwords = _stop_words.ENGLISH_STOP_WORDS

RegLog_model = load('reg_log1.joblib')
vectorization = load('vetorizacao1.joblib')

app = Flask(__name__)

lista = list()

def fake_news_det(text):
    #data processing
    text = text.lower()
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    text = text.replace("</br>", " ") 
    text = "".join([char for char in text if char not in string.punctuation and not char.isdigit()])
    text = " ".join([token for token in text.split() if token not in stopwords])
    #text vectorization
    text_vect = vectorization.transform([text]).toarray()
    #prediction
    prediction = 'FAKE' if RegLog_model.predict(text_vect) == 0 else 'REAL'
    prediction_proba = round((RegLog_model.predict_proba(text_vect))[0].max()*100, 2)
    lista.clear()
    lista.append((prediction, prediction_proba))
    return lista

@app.route("/")
def home():
     return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news = request.form['news']
        pred = fake_news_det(news)
        print(pred)
        return render_template('home.html', prediction=pred[0][0], prediction_prob=pred[0][1])
    else:
        return render_template('home.html', prediction="Something went wrong")

if __name__ == "__main__":
    app.run()
