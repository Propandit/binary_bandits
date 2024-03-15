from flask import Flask, render_template,request
import pickle


model=pickle.load(open('classifier.pkl','rb'))

app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def  predict():
    CreditScore=request.form.get('CreditScore')
    Geography=request.form.get
    Gender=request.form.get('Gender')
    Age=request.form.get('Age')
    Tenure=request.form.get('Tenure')
    Balance=request.form.get('Balance')
    NumOfProducts=request.form.get('NumOfProducts')
    HasCrCard=request.form.get('HasCrCard')
    IsActiveMember=request.form.get('IsActiveMember')
    EstimatedSalary=request.form.get('EstimatedSalary')
    Exited=request.form.get('Exited')

    print(model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Exited]]))

    return "hello world"
if __name__ == '__main__':
    app.run(debug = True)
