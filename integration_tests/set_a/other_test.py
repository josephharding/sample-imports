
import unittest


class OtherTest(unittest.TestCase):


#    def __init__(self, testName, extra):
#        super(OtherTest, self).__init__(testName)
#        self.settings = extra

    @classmethod
    def setUpClass(self, settings):
        print("setUpClass called other test") 
        self.hello = "test"
        self.settings = settings


    def test_number(self):
        self.assertEqual(16, self.settings['age'])


    def test_hello(self):
        self.assertEqual("test", self.hello)
