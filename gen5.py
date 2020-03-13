
import unittest


class RunnerTestCase(unittest.TestCase):


    @classmethod
    def load_runner_settings(self):
        print("hey hey I am RunnerTestCase")
        self.name = "joe"
        return 16


if __name__ == '__main__':
    suite_a = unittest.TestLoader().discover("integration_tests", pattern="*.py")
    suite_b = unittest.TestLoader().discover("integration_tests/set_a", pattern="*.py")
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite([suite_a, suite_b]))
