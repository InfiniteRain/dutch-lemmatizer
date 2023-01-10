import spacy
import nltk
from nltk.corpus import stopwords
from flask import Flask, request, jsonify

nltk.download('stopwords')

stopword_list = stopwords.words('dutch')
nlp = spacy.load("nl_core_news_sm")
app = Flask(__name__)

def lemmatize(text):
    text = text.replace("\n", "").strip()
    docs = nlp.pipe([text])
    cleaned_lemmas = [[t.lemma_ for t in doc] for doc in docs]
    return cleaned_lemmas[0]


@app.route("/")
def index():
    query = request.args.get("query", "")
    if query == "":
        return jsonify([])
    return jsonify(lemmatize(query))
