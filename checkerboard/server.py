from flask import Flask, render_template
app = Flask(__name__)


@app.route('/test')
def test():
    return 'My Checkerboard, test!' 

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/x_row')
def x_row(): 
    return render_template('index2.html')

@app.route('/xy_row') ## challenge not accepted :) 
def xy_row():
    pass


if __name__=="__main__":
    app.run(debug=True)