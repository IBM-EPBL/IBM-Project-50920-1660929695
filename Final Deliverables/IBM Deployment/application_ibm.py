from flask import Flask, render_template, request, send_from_directory
import os
import requests
import json


API_KEY = "Vcb-0L_n80KEcyhvWAPFC4mL6PJvkRMmXqr_zjQsGCIX"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)


@app.route('/')
def helloworld():
    return render_template("home.html")


@app.route('/login', methods = ['POST'])
def login():
    a = request.form["age"]
    b = request.form["bp"]
    c = request.form["sg"]
    d = request.form["alb"]
    e = request.form["sugar"]
    f = request.form["RBC"]
    g = request.form["bacteria"]
    h = request.form["bgr"]
    i = request.form["bu"]
    j = request.form["sc"]
    k = request.form["sodium"]
    l = request.form["haemo"]
    m = request.form["pcv"]
    n = request.form["rbc-count"]
    o = request.form["hypertension"]
    p = request.form["pe"]

    t = [[float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h), float(i), float(j), float(k), float(l), float(m), float(n), float(o), float(p)]]
    print(t)
    payload_scoring =({"input_data": [{"fields": ('f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15'), "values": t}]})

    
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3b650479-b7c6-4d6f-a4bf-aa22108a8222/predictions?version=2022-11-26',json=payload_scoring,  
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    pred=response_scoring.json()
        
    output=pred['predictions'][0]['values'][0][0]
    if(output == 1):
        ans = "Postive"
    else:
        ans = "Negative"
    return render_template("home.html", y = "The predicted result is: "  + ans )

@app.route('/admin')
def admin():
    return "Hey Admin How are you?"

app.run(host='localhost', port=5000)
if __name__ == '__main__' :
    app.run(debug = True)