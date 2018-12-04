class News:
    '''
    News class to define News Object
    '''

    def __init__(self,id,name,description,url,category,language,country):

        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Article:
    '''
    Article class to define Articles objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Topic:
    '''
    Topic class to define Topic objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Headline:
    '''
    Headline class to define Headline objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
