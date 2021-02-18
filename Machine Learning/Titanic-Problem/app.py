from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Titanic-Notebook.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Pclass = int(request.form['Pclass'])
        Sex = request.form['Sex']
        if(Sex=='female'):
            Sex=1
        else:
            Sex=0
        Age = int(request.form['Age'])
        if Age <=16:
            Age=0
        elif Age>16 and Age<=32:
            Age=1
        elif Age>32 and Age<=48:
            Age=2
        elif Age>48 and Age<=64:
            Age=3
        else:
            Age=4
        Fare = float(request.form['Fare'])
        if Fare <=7.91:
            Fare=0
        elif Fare>7.91 and Fare<=14.454:
            Fare=1
        elif Fare>14.454 and Fare<=31:
            Fare=2
        elif Fare>31 and Fare<=64:
            Fare=3

        Embarked = request.form['Embarked']
        if(Embarked=='s'):
            Embarked=0
        elif(Embarked=='c'):
            Embarked=1
        else:
            Embarked=2
        Title = request.form['Title']
        if Title=="Mr":
            Title=1
        elif Title=="Miss":
            Title=2
        elif Title=="Mrs":
            Title=3
        elif Title=="Master":
            Title=4
        else:
            Title=5

        IsAlone = int(request.form['IsAlone'])
        prediction = model.predict([[Pclass,Sex,Age,Fare,Embarked,Title,IsAlone]])
        
        output=round(prediction[0],2)
        
        if output==0:
            #print(output)
            return render_template('index.html',prediction_text="Person Not Survived")
        else:
            return render_template('index.html',prediction_text="Person Survived")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)