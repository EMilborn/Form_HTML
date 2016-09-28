from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def getForm():
    return render_template('form.html', name01 = "TEXT GOES HERE")

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
