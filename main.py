from flask import *
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('Landing.html')

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('Home.html')

@app.route('/account', methods = ['POST', 'GET'])
def account():
    if request.method == 'POST':
        return render_template('Account.html')

@app.route('/lesson-1', methods = ['POST', 'GET'])
def example():
    if request.method == 'POST':
        return render_template('Example.html')

if __name__ == '__main__':
   app.run(debug = True)