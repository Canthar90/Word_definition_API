from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def definition_ednpoint(word):
    output = {"definition": word.upper(),
              "word": word}
    return output


if __name__ == "__main__":
    app.run(debug=True, port=5001)