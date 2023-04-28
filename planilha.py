from flask import  Flask, render_template 
import pandas as pd


app = Flask(__name__)

df = pd.read_csv("data.csv")
df.to_csv("data.csv", index=None)

@app.route('/index')
def home():
    data = pd.read_csv("data.csv")
    return render_template("index.html", tables=[data.to_html()], titles=[])

if __name__ == "__main__":
    app.run(host="localhost", port=int(5000))