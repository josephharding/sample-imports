
import __main__
from inspect import getmodulename
from importlib import import_module


class AnimalTest(import_module(getmodulename(__main__.__file__)).RunnerTestCase):


    @classmethod
    def setUpClass(self):
        print("setUpClass called animal test") 
        self.settings = self.load_runner_settings()
        self.hello = "test"


    def test(self):
        self.assertEqual("joe", self.name)


    def test_age(self):
        self.assertEqual(16, self.settings)


    def test_hello(self):
        self.assertEqual("test", self.hello)
