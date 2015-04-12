from challenge import Challenge, Request
from nose.tools import assert_equals, assert_in
# from nose.plugins.skip import SkipTest


class TestChallenge():
    def test_process_input(self):
        """Handles the input"""
        challenge = Challenge('1 2 3 5')
        challenge.run()
        expected = Request(operands=['1', '2', '3'], result=5)
        assert_equals(expected, challenge.request)

    def test_evaluate_expression(self):
        """Processes a combination of operands and operators"""
        challenge = Challenge('2 3 1 5')
        operands = ['2', '3', '1']
        operators = ['+', '*']
        result = challenge.evaluate_expression(operands, operators)
        assert_equals(result, 5)

    def test_example_three_num_one(self):
        """Handles '1 2 3 5'"""
        challenge = Challenge('1 2 3 5')
        result = challenge.run()
        possible_results = [
            '2 + 3 * 1',
            '3 + 2 * 1'
        ]

        assert_in(result, possible_results)

    def test_example_three_num_two(self):
        """Handles '4 6 3 2'"""
        challenge = Challenge('4 6 3 2')
        result = challenge.run()
        possible_results = [
            '4 * 3 / 6',
            '4 / 6 * 3',
        ]

        assert_in(result, possible_results)

    def test_example_three_num_three(self):
        """Handles '1 1 1 6'"""
        challenge = Challenge('1 1 1 6')
        result = challenge.run()
        assert_equals(result, 'Invalid')

    def test_example_five_num_one(self):
        """Handles '6 7 1 2 5 8'"""
        challenge = Challenge('6 7 1 2 5 8')
        result = challenge.run()
        possible_results = [
            '6 + 5 - 7 * 1 * 2',
            '6 * 7 * 1 - 2 / 5',
        ]

        assert_in(result, possible_results)

    def test_example_five_num_two(self):
        """Handles '1 2 3 4 5 6 3'"""
        challenge = Challenge('1 2 3 4 5 6 3')
        result = challenge.run()
        possible_results = [
            '1 + 2 + 3 + 6 - 4 - 5',
            '1 + 2 + 3 - 4 - 5 + 6',
        ]

        assert_in(result, possible_results)

    def test_format_output(self):
        """Test that formatting the output works as expected"""
        challenge = Challenge('1 2 3 0')
        operands = ('1', '2', '3',)
        operators = ('+', '-',)
        result = challenge.format_output(operands, operators)
        expected = '1 + 2 - 3'
        assert_equals(result, expected)
