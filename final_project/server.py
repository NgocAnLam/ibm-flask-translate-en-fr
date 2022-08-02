from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishToFrench(textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.frenchToEnglish(textToTranslate)


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
