from flask import Flask , render_template , request
import pickle
# print(flask.__version__)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['post'])
def f1():
    age = int(request.form["age"])
    sex = 0 if request.form["sex"] == "male" else 1
    bmi = int(request.form["bmi"])
    children = int(request.form["children"])
    smoker = 0 if request.form["smoker"] == "no" else 1
    print(request.form)
    # age,sex,bmi,children,smoker = 25,0,25.0,0,1
    scaler = pickle.load(open("scaler_obj.pkl","rb"))
    model = pickle.load(open("health_insu.pkl","rb"))
    q=[[age,sex,bmi,children,smoker]]
    q_scaled=scaler.transform(q)
    yp=round(model.predict(q_scaled)[0],2)                       # square brackets used bcz without it comes in list format
    return render_template("result.html", prediction=yp)

if __name__=="__main__":
    app.run(debug=True)