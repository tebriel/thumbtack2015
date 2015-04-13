#!/usr/bin/env python3

import sys
from collections import namedtuple
from itertools import combinations_with_replacement, permutations

Request = namedtuple('Request', ['operands', 'result'])
OPERATORS = ['+', '-', '*', '/']


class Challenge(object):
    """PyCon2015 Thumbtack Challenge Solution"""

    def __init__(self, str_input):
        """Prep ourselves for fun computations"""

        # Strip the \n from the input for __repr__ later
        self.str_input = str_input.strip()
        inputs = str_input.split(' ')
        self.request = Request(operands=inputs[:-1], result=int(inputs[-1]))

    def __repr__(self):
        """Show how to recreate ourselves"""

        return "Challenge('%s')" % (self.str_input)

    @staticmethod
    def evaluate(numbers, operators):
        """Sets our left to right order of operations, then evaluates it"""

        to_exe = ""
        for operator in operators:
            a = numbers.pop(0)
            b = numbers.pop(0)
            to_exe = "(%s %s %s)" % (a, operator, b)
            numbers.insert(0, to_exe)

        return eval(numbers[0])

    @staticmethod
    def format_output(operands, operators):
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
        total_digits = len(self.request.operands)

        operand_perms = permutations(self.request.operands, total_digits)

        # Try each one
        for operand_perm in operand_perms:
            operator_combos = combinations_with_replacement(OPERATORS,
                                                            total_digits - 1)
            # Get all the possible combinations (with repeats) of the operators
            # Try each one
            for operator_combo in operator_combos:
                operator_perms = permutations(operator_combo,
                                              len(operator_combo))
                for operator_perm in operator_perms:
                    result = self.evaluate(list(operand_perm), operator_perm)

                    if result == self.request.result:
                        return self.format_output(operand_perm, operator_perm)

        return 'Invalid'

if __name__ == '__main__':
    for line in sys.stdin:
        challenge = Challenge(line)
        print(challenge.run())
