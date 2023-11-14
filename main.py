from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/v1/<word>")
def translate(word):
    df = pd.read_csv("Files/dictionary.csv")
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    dict= {"word": word, "definition": definition
           }
    return(dict)

app.run(debug=True)