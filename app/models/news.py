class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,source,headlines,overview,image):
        self.source = source
        self.headlines = headlines
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500/'+image
       