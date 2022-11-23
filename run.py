from flask import Flask, app, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tambahdata')
def tambahdata():
    return render_template('tambahdata.html')

@app.route('/listdata')
def listdata():
    return render_template('listdata.html')

@app.route('/login')
def login():
    return render_template('login.html') 

if __name__=="__main__":
    app.run(debug=True)