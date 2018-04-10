import urllib.request, json
from .models import News, Article


# Getting api key
api_key = None

#Getting the news sources and the articles base url
base_url = None
a_base_url = None

def configure_request(app):
    global api_key,base_url,a_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL'] 
    # a_base_url = app.config['ARTICLES_API_BASE_URL'] 


def process_results(news_list):
        '''
        Function  that processes the news result and transform them to a list of Objects

        Args:
            news_list: A list of dictionaries that contain news details

        Returns :
            news_results: A list of news objects
        '''
        news_results = []
        for news_item in news_list:
            id = news_item.get('id')
            name = news_item.get('name')
            description = news_item.get('description')
            url = news_item.get('url')
            category = news_item.get('category')
            language = news_item.get('language')
            country = news_item.get('country')

            news_results.append(News(id,name,description,url,category,language,country))

        return news_results 


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results



def process_articles(articles_list):
        '''
        Function  that processes the news result and transform them to a list of Objects

        Args:
            news_list: A list of dictionaries that contain news details

        Returns :
            news_results: A list of news objects
        '''
        articles_results = []
        for article in articles_list:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')
            
            news_article = Article(author,title,description,url,urlToImage,publishedAt)

            articles_results.append(news_article)

        return articles_results

def get_articles(id):
    get_articles_url = base_url.format("everything", api_key) + "&sources=" + id
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_details_data = url.read()
        get_articles_response = json.loads(articles_details_data)
        # print(get_articles_response)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)



    return articles_results








      
    #     if articles_details_response:
    #         author = articles_details_response.get('author')
    #         title = articles_details_response.get('title')
    #         description = articles_details_response.get('description')
    #         url = articles_details_response.get('url')
    #         urlToImage = articles_details_response.get('urlToImage')
    #         publishedAt = articles_details_response.get('publishedAt')

    #     if urlToImage:
    #         articles_object = Article(author,title,description,url,urlToImage,publishedAt)
    #         articles_results.append(articles_object)


    # return articles_object


