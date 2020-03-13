
import sys
sys.path.append("../..")

import importlib

import __main__
my_module = importlib.import_module(__main__.__file__.split(".")[0])


class OtherTest(my_module.RunnerTestCase):


    @classmethod
    def setUpClass(self):
        print("setUpClass called animal test") 
        self.settings = self.load_runner_settings()
        self.hello = "test"


    def test_number(self):
        self.assertEqual(16, self.settings)


    def test_hello(self):
        self.assertEqual("test", self.hello)
