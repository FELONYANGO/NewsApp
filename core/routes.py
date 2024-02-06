from core import app
from flask import render_template
from .utils import news


@app.route('/')
def news_headlines():
    news_articles = news()
    return render_template("index.html", news_articles=news_articles)
