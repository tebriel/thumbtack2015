#!/usr/bin/env python3

import sys
from collections import namedtuple
from itertools import combinations_with_replacement, permutations

Request = namedtuple('Request', ['operands', 'result'])
OPERATORS = ['+', '-', '*', '/']


class Challenge(object):
    """PyCon2015 Thumbtack Challenge Solution"""

    @staticmethod
    def evaluate_expression(numbers, operators):
        """Sets our left to right order of operations, then evaluates it"""

        to_exe = ""
        for operator in operators:
            a = numbers.pop(0)
            b = numbers.pop(0)
            to_exe = "(%s %s %s)" % (a, operator, b)
            numbers.insert(0, to_exe)

        return eval(numbers[0])

    def __init__(self, str_input):
        """Prep ourselves for fun computations"""

        # Strip the \n from the input for __repr__ later
        self.str_input = str_input.strip()
        inputs = str_input.split(' ')
        self.request = Request(operands=inputs[:-1], result=int(inputs[-1]))

    def __repr__(self):
        """Show how to recreate ourselves"""

        return "Challenge('%s')" % (self.str_input)

    def format_output(self, operands, operators):
        """Creates the output string for a completed challenge"""
        # Append a space to make zip work properly results in '+ '
        operators = operators + (' ',)
        result = []
        for idx, operand in enumerate(operands):
            result.append("%s %s" % (operand, operators[idx]))

        return ' '.join(result).strip()

    def run(self):
        """Tries all pemutations of operands with all combinations (with
        replacement of the operators)"""

        # Get all the permutations of our operands
        permutes = permutations(self.request.operands,
                                len(self.request.operands))
        # Try each one
        for permute in permutes:
            # Get all the possible combinations (with repeats) of the operators
            combos = combinations_with_replacement(OPERATORS, len(permute) - 1)
            # Try each one
            for combo in combos:
                result = self.evaluate_expression(list(permute), combo)

                if result == self.request.result:
                    return self.format_output(permute, combo)

        return 'Invalid'

if __name__ == '__main__':
    for line in sys.stdin:
        challenge = Challenge(line)
        print(challenge.run())
