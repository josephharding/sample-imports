
import unittest


class OtherTest(unittest.TestCase):


    def __init__(self, testName, extra):
        super(OtherTest, self).__init__(testName)
        self.settings = extra

    @classmethod
    def setUpClass(self):
        print("setUpClass called animal test") 
        self.hello = "test"


    def test_number(self):
        self.assertEqual(16, self.settings)


    def test_hello(self):
        self.assertEqual("test", self.hello)
