import crimeMap.dbconfig as dbconfig
from flask import Flask
from flask import render_template
from flask import request


if dbconfig.test:
    from crimeMap.mockDBHelper import MockDBHelper as DBHelper
else:
    from crimeMap.dbHelper import DBHelper

app = Flask(__name__)
DB = DBHelper()

@app.route("/")

def home():
    try:
        data = DB.getAllInputs()
    except Exception as e:
        print(e)
        data = None
    return render_template("home.html", data=data)

@app.route("/add", methods=["POST"])

def add():
    try:
        data = request.form.get("input")
        if data:
            DB.addInput(data)
    except Exception as e:
        print(e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clearAll()
    except Exception as e:
        print(e)
    return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
