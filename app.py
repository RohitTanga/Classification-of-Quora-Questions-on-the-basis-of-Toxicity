from flask import Flask,render_template,url_for
import requests
from flask import request as req
from prediction import md
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')
@app.route("/classify",methods=['GET','POST'])
def classify():
    # print(req.method)
    
    if req.method=='POST':
        
        data=req.form.get("data",False)
        prediction=obj.predict(data)
        print(prediction)
        prediction = 'insincere' if prediction else 'sincere'
        return render_template('index.html',out=prediction)
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    obj=md()
    app.debug=True
    app.run()
