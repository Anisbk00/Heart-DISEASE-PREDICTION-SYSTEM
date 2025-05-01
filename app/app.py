from flask import Flask,request,jsonify
import joblib
import pandas as pd

app=Flask(__name__)
model=joblib.load("../app/model/heart_disease_rf_model.pkl")

#definig route
@app.route("/predict",methods=["POST"])
def predict():
    data =request.json
    print(data)
    try:
        input_data=pd.DataFrame([data])
        print(input_data)
        prediction=model.predict(input_data)[0]
        return jsonify({"Prediction: ",int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}),400

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)