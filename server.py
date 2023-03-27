from flask import Flask
app = Flask(__name__)

@app.route('/')  #challenge 1: localhost says "hello world"
def hello_world ():
    return "Hello World" 

@app.route("/dojo") #challegen 2: localhost says "dojo"
def dojo (): 
    return "Dojo!"

@app.route("/say/flask")
def say_flask (): 
    return "Hi " + "Flask"

@app.route("/say/<string:name>") #challenge 3: localhost prints out name with input i.e.  "Hello Michael" or "Hello John"
def say_name(name): 
    print(name)
    return f"Hello + {name}" 

@app.route("/repeat/<string:name>/<int:num>") #challenge 4: local host prints out names * times i.e 35x, 80x, 99x 
def repeat_string(name, num): 
    return f"Hello {name * num}"

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)
