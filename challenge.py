#!/usr/bin/env python3

import sys
from collections import namedtuple

Request = namedtuple('Request', ['operands', 'result'])


class Challenge(object):
    def __init__(self):
        pass

    def run(self, str_input):
        self.process_input(str_input)
        if self.is_too_small():
            return 'Invalid'
        else:
            raise NotImplementedError

    def process_input(self, str_input):
        inputs = str_input.split(' ')
        operands = [int(n) for n in inputs[:-1]]
        self.request = Request(operands=operands, result=int(inputs[-1]))

    def is_too_small(self):
        return False


if __name__ == '__main__':
    challenge = Challenge()
    for line in sys.stdin:
        print(challenge.run(line))
