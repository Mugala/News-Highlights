from flask import render_template,redirect,request,url_for
from . import main
from ..request import get_news,get_articles,get_topic,search_news,headline_news


#views
@main.route('/')
def index():
    """
    Root page returns the home page for news HIGHLIGHTS
    """
    title = "Catch up with what has been happening around the globe"
    News_sources = get_news()

    search_news = request.args.get('news_query')


    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('home.html',title=title,sources=News_sources)


@main.route('/sources')
def sources():
    """
    Page that displays the news sources as well as the link to articles and website
    """
    title = "Catch up with what has been happening around the globe"
    News_sources = get_news()

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('sources.html',title=title,sources=News_sources)

@main.route('/articles/<id>')
def article(id):
    '''
    View function page for all the articles for a specific sources
    '''

    articles_sources = get_articles(id)
    title = 'News articles'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('articles.html',title=title,articles=articles_sources)

@main.route('/search/<topic_news>')
def search(topic_news):
    '''
    View function to display the search results
    '''

    news_name_list = topic_news.split(' ')
    news_name_format = '+'.join(news_name_list)
    searched_topics = get_topic(news_name_format)
    title = f'search results for {topic_news}'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('search.html',news_topics = searched_topics, t =topic_news,title=title)

@main.route('/headline/<topic>')
def headlines(topic):
    '''
    View function to display the headlines results
    '''

    news_headlines = headline_news(topic)

    search_news = request.args.get('news_query')
    title = f'headlines for {topic}'

    if search_news:
        return redirect(url_for('main.search',topic_news = search_news))
    else:
        return render_template('headlines.html',headlines = news_headlines, title=title,t=topic)
