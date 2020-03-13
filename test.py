
import unittest


class AnimalTest():


    @classmethod
    def init(self):
        self.hello = "test"


    def test(self):
        self.assertEqual("joe", self.name)


    def test_age(self):
        self.assertEqual(16, self.age)


    def test_hello(self):
        self.assertEqual("test", self.hello)


class CatTest(unittest.TestCase, AnimalTest):


    @classmethod
    def setUpClass(self):
        print("setUpClass called")
        self.age = 16
        super(CatTest, self).init()

    def setUp(self):
        print("setUp called")
        self.name = "joe"


if __name__ == '__main__':
    unittest.main(verbosity=2)
