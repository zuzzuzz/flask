from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play') #localhost creates 3 red boxes 
def challenge_one():
    return render_template("index.html", num=3, color="red")

@app.route('/play/<int:num>') #local host creates x number of identical boxes 
def challenge_two(num):
    return render_template("index.html", num=num, color="red")

@app.route('/play/<int:num>/<string:color>') #local host changes color of boxes input by user
def challenge_three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

