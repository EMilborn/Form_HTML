from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def getForm():
    return render_template('form.html',
                           name01 = "TEXT GOES HERE",
                           heading01 = "HEADING")

@app.route("/authenticate/")
def auth():
    print request.headers
    return "OK"

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
