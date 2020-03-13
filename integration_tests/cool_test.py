
import sys

sys.path.append("..")

from test_unit import RunnerTestCase


class AnimalTest(RunnerTestCase):


    @classmethod
    def setUpClass(self):
        print("setUpClass called animal test") 
        #super(AnimalTest, self).init()
        self.settings = self.load_runner_settings()
        self.hello = "test"


    def test(self):
        self.assertEqual("joe", self.name)


    def test_age(self):
        self.assertEqual(16, self.settings)


    def test_hello(self):
        self.assertEqual("test", self.hello)
