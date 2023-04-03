from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key='this is a secret'

@app.route('/')
def index(): 
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/addOne', methods=['POST'])
def addOne():
    session['count'] += 1
    return redirect('/')


@app.route('/addTwo', methods=['POST'])
def addTwo():
    session['count'] += 2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count']=0
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True) 
