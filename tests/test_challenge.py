from challenge import Challenge, Request
from nose.tools import assert_equals  # , assert_true, assert_false
# from nose.plugins.skip import SkipTest


class TestChallenge():
    def setup(self):
        self.challenge = Challenge()

    def test_process_input(self):
        """Handles the input"""
        self.challenge.process_input('1 2 3 5')
        expected = Request(operands=['1', '2', '3'], result=5)
        assert_equals(expected, self.challenge.request)

    def test_example_three_num_one(self):
        """Handles '1 2 3 5'"""
        result = self.challenge.run('1 2 3 5')
        assert_equals(eval(result), eval('3 + 2 * 1'))

    def test_example_three_num_two(self):
        """Handles '4 6 3 2'"""
        result = self.challenge.run('4 6 3 2')
        assert_equals(eval(result), eval('4 / 6 * 3'))

    def test_example_three_num_three(self):
        """Handles '1 1 1 6'"""
        result = self.challenge.run('1 1 1 6')
        assert_equals(result, 'Invalid')

    def test_example_five_num_one(self):
        """Handles '6 7 1 2 5 8'"""
        result = self.challenge.run('6 7 1 2 5 8')
        assert_equals(eval(result), eval('6 * 7 * 1 - 2 / 5'))

    def test_example_five_num_two(self):
        """Handles '1 2 3 4 5 6 3'"""
        result = self.challenge.run('1 2 3 4 5 6 3')
        assert_equals(eval(result), eval('1 + 2 + 3 - 4 - 5 + 6'))
