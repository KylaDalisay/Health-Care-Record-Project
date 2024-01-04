from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
 return render_template('halcyonCenter.html')
  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  return render_template('signup.html')

@app.route('/doctorsHomepage')
def hospitalhomepage():
  return render_template('hospitalhomepage.html')

@app.route('/personelInformation')
def doctorhomepage():
    return render_template('personelInformation.html')

@app.route('/addPatient')
def addPatient():
  return render_template('')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
