from flask import render_template
from .request import get_news,get_articles
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
     # Getting news sources
    news_source = get_news('sources')
    print(news_source)
    title = 'Home - Get The News at your Convenience when they Break'
    return render_template('index.html', title = title, source = news_source)


@app.route('/article/<id>')
def article(id):
    '''
    View articles page function for all the articles for specific source
    '''
    articles_sources = get_articles('articles')


    articles_sources = get_articles(id)
    # title = f'{article.title}'
    title = 'Home - Get The News articles'

    return render_template('news.html', title=title, article = articles_sources)

    

