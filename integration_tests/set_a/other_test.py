
import sys
sys.path.append("../..")

from test_unit import RunnerTestCase


class OtherTest(RunnerTestCase):


    @classmethod
    def setUpClass(self):
        print("setUpClass called animal test") 
        self.settings = self.load_runner_settings()
        self.hello = "test"


    def test_number(self):
        self.assertEqual(16, self.settings)


    def test_hello(self):
        self.assertEqual("test", self.hello)
