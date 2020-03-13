
import sys
import importlib

sys.path.append("..")

import __main__
my_module = importlib.import_module(__main__.__file__.split(".")[0])

class AnimalTest(my_module.RunnerTestCase):


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
