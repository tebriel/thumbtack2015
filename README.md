# Thumbtack Code Challenge! #

[![Build Status](https://travis-ci.org/tebriel/thumbtack2015.svg?branch=master)](https://travis-ci.org/tebriel/thumbtack2015)

Write a Python program that takes in four numbers and determines the
mathematical express than can combine the first three numbers, through
addition, subtraction, multiplication, and division, to get the fourth.

*  Input will be a space-separated string of four positive integers on `stdin`.
*  Expressions will simply be evaluated left-to-right, ignoring traditional
   order of operations.
*  Remember not to use integer division: `5 / 2 = 2.5`
*  For some inputs, there may be many possible valid outputs. You only need to
   print one.
*  For some inputs, there may be no valid output. In this case, print
   `Invalid`.

```sh
$ echo '1 2 3 5' | python challenge.py
$ 3 + 2 * 1

$ echo '4 6 3 2' | python challenge.py
$ 4 / 6 * 3

$ echo '1 1 1 6' | python challenge.py
$ Invalid
```

## Win a Thumbtack beer mug! ##

Same as above, but solve the problem for an arbitrary number of inputs. The
number to solve for will always be the last number in the string, but the total
number of numbers in the string is not constant.

```sh
$ echo '6 7 1 2 5 8' | python challenge.py
$ 6 * 7 * 1 - 2 / 5

$ echo '1 2 3 4 5 6 3' | python challenge.py
$ 1 + 2 + 3 - 4 - 5 + 6
```
