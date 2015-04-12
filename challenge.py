#!/usr/bin/env python3

import sys
from collections import namedtuple
from itertools import combinations_with_replacement, permutations

Request = namedtuple('Request', ['operands', 'result'])
OPERATORS = ['+', '-', '*', '/']


class Challenge(object):

    @classmethod
    def evaluate_expression(cls, numbers, operators):
        """Sets our left to right order of operations, then evaluates it"""
        to_exe = ""
        for operator in operators:
            a = numbers.pop(0)
            b = numbers.pop(0)
            to_exe = "(%s %s %s)" % (a, operator, b)
            numbers.insert(0, to_exe)

        return eval(numbers[0])

    def __init__(self, str_input):
        self.str_input = str_input.strip()
        inputs = str_input.split(' ')
        self.request = Request(operands=inputs[:-1], result=int(inputs[-1]))

    def __repr__(self):
        return "Challenge(%s)" % (self.str_input)

    def run(self):
        permutes = permutations(self.request.operands,
                                len(self.request.operands))
        for permute in permutes:
            combos = combinations_with_replacement(OPERATORS, len(permute) - 1)
            for combo in combos:
                # Make our string
                combo_str = ''.join(combo) + ' '
                groups = list(zip(permute, combo_str))
                seq = ' '.join([' '.join(group) for group in groups]).strip()

                result = self.evaluate_expression(list(permute), combo)

                if result == self.request.result:
                    return seq
        return 'Invalid'

if __name__ == '__main__':
    for line in sys.stdin:
        challenge = Challenge(line)
        print(challenge)
        print(challenge.run())
