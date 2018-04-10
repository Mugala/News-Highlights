import unittest
from app.models import Article


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Article('p.n Boyle','Python Network','Python version 4.0 coming soon','www.pythonnetwork.com','https://media.npr.org/assets/img/2018/04/09/ap_18087317720635_wide-5ac9c7e53323d8121f08d15f7267e8b767482c49.jpg?s=1400','2018-04-09T05:17:12Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Article))

