class TestCaseRegister:
    def __init__(self):
        self._test_cases = []

    def add_test_case(self, test_case):
        self._test_cases.append(test_case)

    def get_all_test_cases(self):
        return self._test_cases