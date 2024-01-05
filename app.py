from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)

@app.route('/')
def hello_world():
 return render_template('halcyonCenter.html')
  
@app.route('/signup', methods=['POST', 'GET'])
def signup():
  
  return render_template('signup.html')

@app.route('/doctorsHomepage', methods=['POST','GET'])
def hospitalhomepage():
  return render_template('hospitalhomepage.html')

@app.route('/personelInformation')
def doctorhomepage():
    return render_template('personelInformation.html')

@app.route('/addPatient')
def addPatient():
  return render_template('addPatient.html')

@app.route('/patientlist')
def patientlist():
  return render_template('patientlist.html')

@app.route('/personelpatientdetailes')
def personelpatientdetailes():
  return render_template("personelpatientdetailes.html")

@app.route("/personelpatientsdrescription")
def personelpatientsmedicalhistory():
  return render_template("personelpatientsmedicalhistory.html")

@app.route("/personelpatientsmedicalhistorylist")
def personelpatientsprescription():
  return render_template("personelpatientdetails.html")

@app.route("/personelpatientaddnewmedicalhistory")
def personelpatientaddnewmedicalhistory():
  return render_template("personelpatientdetails.html")

@app.route("/hospitaladdnewpatient")
def hospitaladdnewpatient():
  return render_template("hospitaladdnewpatient.html")

@app.route("/forgetpassword")
def forgetpassword():
  return render_template("forgetpassword.html")

@app.route("/newpassword")
def newpassword():
  return render_template("newpassword.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
