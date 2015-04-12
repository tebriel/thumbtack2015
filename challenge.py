#!/usr/bin/env python3

import sys


class Challenge(object):
    def __init__(self):
        pass

    def run(self, input):
        return 'Invalid'

if __name__ == '__main__':
    challenge = Challenge()
    for line in sys.stdin:
        print(challenge.run(line))
