from flask import Flask, jsonify, Response, render_template, request
import numpy as np
import pandas as pd
from utils import deposite
import pickle
app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Welcome to Project Term Deposite Prediction')
    return render_template('index.html')


@app.route('/predict', methods = ['GET','POST'])
def prediction():
    data = request.form
    if request.method == 'POST':
        age = eval(data['age'])
        marital = data['marital']
        balance = eval(data['balance'])
        housing = data['housing']
        loan = data['loan']
        contact = data['contact']
        day = eval(data['day'])
        duration = eval(data['duration'])
        campaign = eval(data['campaign'])
        previous = eval(data['previous'])
        job = data['job']
        education = data['education']
        month = data['month']
        poutcome = data['poutcome']
        subscription = deposite(age, marital, balance, housing, loan, contact, day, duration, 
                                campaign, previous, job, education, month, poutcome)
    
        if subscription==0:
            result="Client Not Subscribed Term Deposite"
        elif subscription==1:
            result="Client Subscribed Term Deposite"
    return render_template('after.html',prediction=result)

if __name__=="__main__":
    app.run(debug=True)