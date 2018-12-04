import urllib.request,json
from .models import News, Article,Topic,Headline

#Getting the API Key
api_key = None
#Getting the news base url
base_url = None
def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format('sources',api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_sources = json.loads(get_news_data)

        news_sources_results = None

        if get_news_sources['sources']:
            sources_results_list = get_news_sources['sources']
            news_sources_results = process_results(sources_results_list)


    return news_sources_results


def process_results(sources_list):
    '''
    Function that process the sources and transform them to a list of objects
    '''

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        sources_results.append(News(id,name,description,url,category,language,country))

    return sources_list

def get_articles(id):
        get_articles_url = base_url.format('everything',api_key) + '&sources='+ id

        with urllib.request.urlopen(get_articles_url) as url:
            get_articles_data = url.read()
            get_articles_response = json.loads(get_articles_data)

            news_articles_results = None

            if get_articles_response['articles']:
                articles_results_list = get_articles_response['articles']
                news_articles_results = process_articles_results(articles_results_list)


        return news_articles_results

def process_articles_results(articles_list):
    '''
    Function that process the articles and transforms them to a list of objects
    '''

    articles_results =[]
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        articles_results.append(Article(author,title,description,url,urlToImage,publishedAt))


    return articles_list

def get_topic(topic_news):
    get_topic_url = base_url.format('everything',api_key) + '&q=' + topic_news

    with urllib.request.urlopen(get_topic_url) as url:
        get_topic_data = url.read()
        get_topic_response = json.loads(get_topic_data)

        news_topic_results = None

        if get_topic_response['articles']:
            topic_results_list = get_topic_response['articles']
            news_topic_results = process_topic_results(topic_results_list)

    return news_topic_results

def process_topic_results(topic_list):
    '''
    Function that process the topics and transforms them to a list of objects
    '''

    topic_results = []
    for topic_item in topic_list:
        author = topic_item.get('author')
        title = topic_item.get('title')
        description = topic_item.get('description')
        url = topic_item.get('url')
        urlToImage = topic_item.get('urlToImage')
        publishedAt = topic_item.get('publishedAt')

        topic_results.append(Topic(author,title,description,url,urlToImage,publishedAt))

    return topic_list

def search_news(topic_news):
    search_news_url = 'https://newsapi.org/v2/everything?apiKey={}&q={}'.format(api_key,topic_news)

    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None


        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_topic_results(search_news_list)

    return search_news_results

def process_headline_results(headline_list):
    '''
    Function that process the headlines and transforms them to a list of objects
    '''

    headline_results = []
    for headline_item in headline_list:
        author = headline_item.get('author')
        title = headline_item.get('title')
        description = headline_item.get('description')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')

        headline_results.append(Headline(author,title,description,url,urlToImage,publishedAt))

    return headline_list


def headline_news(topic):
    headline_news_url = 'https://newsapi.org/v2/top-headlines?apiKey={}&category={}'.format(api_key,topic)

    with urllib.request.urlopen(headline_news_url) as url:
        headline_news_data = url.read()
        headline_news_response = json.loads(headline_news_data)

        headline_news_results = None


        if headline_news_response['articles']:
            headline_news_list = headline_news_response['articles']
            headline_news_results = process_headline_results(headline_news_list)

    return headline_news_results
