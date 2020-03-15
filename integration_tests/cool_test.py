
import unittest


class AnimalTest(unittest.TestCase):


#    def __init__(self, testName, extra):
#        super(AnimalTest, self).__init__(testName)
#        print("the init method is being called")
#        self.settings = extra


    @classmethod
    def setUpClass(self, settings):
        print("setUpClass called animal test") 
        self.hello = "test"
        self.settings = settings


    def test_age(self):
        self.assertEqual(16, self.settings['age'])


    def test_hello(self):
        self.assertEqual("test", self.hello)
