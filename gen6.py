
import unittest


def _call_if_exists(parent, attr):
    func = getattr(parent, attr, lambda: None)
    func()


class _DebugResult(object):
    "Used by the TestSuite to hold previous class when running in debug."
    _previousTestClass = None
    _moduleSetUpFailed = False
    shouldStop = False


if __name__ == '__main__':

    some_big_fat_dict = {}
    some_big_fat_dict['hey'] = "hello"
    some_big_fat_dict['age'] = 16

    class CustomTestSuite(unittest.TestSuite):

        def _handleClassSetUp(self, test, result):
            currentClass = test.__class__
            setUpClass = getattr(currentClass, 'setUpClass', None)
            if setUpClass is not None:
                setUpClass(some_big_fat_dict)



    class CustomTestLoader(unittest.TestLoader):

        suiteClass = CustomTestSuite

        def loadTestsFromTestCase(self, testCaseClass):
            test_cases = []
            for test_case_name in self.getTestCaseNames(testCaseClass):
                test_cases.append(testCaseClass(test_case_name))
            return self.suiteClass(test_cases)


    suite_a = CustomTestLoader().discover("integration_tests", pattern="*.py")
    suite_b = CustomTestLoader().discover("integration_tests/set_a", pattern="*.py")

    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite([suite_a, suite_b]))
