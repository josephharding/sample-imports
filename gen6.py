
import unittest


if __name__ == '__main__':


    class CustomTestLoader(unittest.TestLoader):


        def loadTestsFromTestCase(self, testCaseClass):
            test_cases = []
            for test_case_name in self.getTestCaseNames(testCaseClass):
                test_cases.append(testCaseClass(test_case_name, 16))
            return self.suiteClass(test_cases)


    suite_a = CustomTestLoader().discover("integration_tests", pattern="*.py")
    suite_b = CustomTestLoader().discover("integration_tests/set_a", pattern="*.py")

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite([suite_a, suite_b]))
