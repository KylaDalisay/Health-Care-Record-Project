from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
 return render_template('halcyonCenter.html')
  
@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/hospitalHomepage')
def hospitalhomepage():
  return render_template('signup.html')

@app.route('/hospitalinformati')

@app.route('/doctorHomepage')
  def doctorhomepage():
    return render_template():
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
