#!/usr/bin/env python3

import sys
from collections import namedtuple
from itertools import combinations_with_replacement

Request = namedtuple('Request', ['operands', 'result'])
OPERATORS = ['+', '-', '*', '/']


class Challenge(object):

    def __init__(self):
        pass

    def run(self, str_input):
        self.process_input(str_input)
        return self.try_combinations()

    def process_input(self, str_input):
        inputs = str_input.split(' ')
        self.request = Request(operands=inputs[:-1], result=int(inputs[-1]))

    def try_combinations(self):
        combos = combinations_with_replacement(OPERATORS,
                                               len(self.request.operands) - 1)
        for combo in combos:
            combo_str = ''.join(combo) + ' '
            groups = list(zip(self.request.operands, combo_str))
            seq = ' '.join([' '.join(group) for group in groups]).strip()
            if eval(seq) == self.request.result:
                return seq
        return 'Invalid'


if __name__ == '__main__':
    challenge = Challenge()
    for line in sys.stdin:
        print(challenge.run(line))
