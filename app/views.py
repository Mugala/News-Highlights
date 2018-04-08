from flask import render_template
from .request import get_news
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
     # Getting news
    days_news = get_news('D_news')
    print(days_news)
    title = 'Home - Get The News at your Convenience when they Break'
    return render_template('index.html', title = title, D_news = days_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''

    return render_template('news.html',id = news_id)


from .request import get_movies

