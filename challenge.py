#!/usr/bin/env python3

import sys
from collections import namedtuple
from itertools import combinations_with_replacement, permutations

Request = namedtuple('Request', ['operands', 'result'])
OPERATORS = ['+', '-', '*', '/']


class Challenge(object):

    @classmethod
    def evaluate_expression(cls, numbers, operators):
        to_exe = ""
        for operator in operators:
            a = numbers.pop(0)
            b = numbers.pop(0)
            to_exe = "(%s %s %s)" % (a, operator, b)
            # total = "%f" % (eval("%s%s%s" % (a, operator, b)))
            numbers.insert(0, to_exe)

        return eval(numbers[0])

    def __init__(self):
        pass

    def run(self, str_input):
        self.process_input(str_input)
        return self.try_combinations()

    def process_input(self, str_input):
        inputs = str_input.split(' ')
        self.request = Request(operands=inputs[:-1], result=int(inputs[-1]))

    def try_combinations(self):
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
    challenge = Challenge()
    for line in sys.stdin:
        print(challenge.run(line))
