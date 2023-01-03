from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import pandas as pd


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def definition_ednpoint(word):
    try:
        df = pd.read_csv("dictionary.csv", encoding="utf-8")
        definition = df.loc[df['word'] == word.lower()]["definition"].squeeze()
        output = {"definition": definition,
                "word": word}
        return jsonify(output)
    except:
        return jsonify(response={"error": "Argument's passed are invalid"}), 404
    
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)