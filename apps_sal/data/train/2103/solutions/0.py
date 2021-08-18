
"""
Input

The first line contains integers n and m - the number of islands and bridges.

Next n lines each contain two integers li and ri - the coordinates of the
island endpoints.

The last line contains m integer numbers a1..am - the lengths of the bridges
that Andrewid got.
Output

If it is impossible to place a bridge between each pair of adjacent islands
in the required manner, print on a single line "No" (without the quotes)
, otherwise print in the first line "Yes" (without the quotes), and in the
second line print n-1 numbers b1, bn-1, which mean that between islands
i and i+1 there must be used a bridge number bi.

If there are multiple correct answers, print any of them. Note that in this
problem it is necessary to print "Yes" and "No" in correct case
"""

import unittest
import sys
import re

import heapq


class Fug:
    """ Fug representation """

    def __init__(self, args):
        """ Default constructor """
        self.list = args[0]
        self.alist = args[1]
        self.gn = len(self.list) - 1

        self.asrt = sorted((n, i) for i, n in enumerate(self.alist))

        self.gaps = [()] * self.gn
        prevli = self.list[0]
        for i in range(self.gn):
            li = self.list[i + 1]
            min = li[0] - prevli[1]
            max = li[1] - prevli[0]
            self.gaps[i] = (min, max, i)
            prevli = li

        self.gsrt = sorted(self.gaps)

        self.gmin = [n[0] for n in self.gsrt]
        self.result = [None] * self.gn
        self.heap = []

    def iterate(self):

        j = 0
        for (b, i) in self.asrt:

            while j < self.gn and self.gmin[j] <= b:
                it = self.gsrt[j]
                heapq.heappush(self.heap, (it[1], it[0], it[2]))
                j += 1

            if self.heap:
                (mmax, mmin, mi) = self.heap[0]
                if mmin <= b and mmax >= b:
                    self.result[mi] = i + 1
                    heapq.heappop(self.heap)

            yield

    def calculate(self):
        """ Main calcualtion function of the class """

        for it in self.iterate():
            pass

        answer = ""
        for (i, n) in enumerate(self.result):
            if n is None:
                return "No"
            answer += (" " if i > 0 else "") + str(n)

        return "Yes\n" + answer


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return input()

    num = [int(s) for s in uinput().split()]
    list = [[int(s) for s in uinput().split()] for i in range(num[0])]
    alist = [int(s) for s in uinput().split()]

    inputs = [list, alist]

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Fug(get_inputs(test_inputs)).calculate()


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        test = "4 4\n1 4\n7 8\n9 10\n12 14\n4 5 3 8"
        self.assertEqual(calculate(test), "Yes\n2 3 1")
        self.assertEqual(
            get_inputs(test),
            [[[1, 4], [7, 8], [9, 10], [12, 14]], [4, 5, 3, 8]])

        test = "5 5\n1 1\n2 7\n8 8\n10 10\n16 16\n1 1 5 6 2"
        self.assertEqual(calculate(test), "Yes\n1 2 5 4")

        test = "2 2\n11 14\n17 18\n2 9"
        self.assertEqual(calculate(test), "No")

        test = (
            "2 1\n1 1\n1000000000000000000 1000000000000000000"
            + "\n999999999999999999")
        self.assertEqual(calculate(test), "Yes\n1")

        test = ("5 9\n1 2\n3 3\n5 7\n11 13\n14 20\n2 3 4 10 6 2 6 9 5")
        self.assertEqual(calculate(test), "Yes\n1 6 3 2")

        size = 100000
        test = str(size) + " " + str(size) + "\n"
        x = size * 1000
        for i in range(size):
            x += 2
            test += str(x) + " " + str(x + 1) + "\n"
        for i in range(size):
            test += str(2) + " "
        self.assertEqual(calculate(test)[0], "Y")

    def test_Fug_class__basic_functions(self):
        """ Fug class basic functions testing """

        d = Fug([[[1, 5], [7, 8], [9, 10], [12, 14]], [4, 5, 3, 8]])
        self.assertEqual(d.list[0][0], 1)
        self.assertEqual(d.alist[0], 4)

        self.assertEqual(d.asrt[0], (3, 2))

        self.assertEqual(d.gaps[0], (2, 7, 0))
        self.assertEqual(d.gsrt[0], (1, 3, 1))

        iter = d.iterate()
        next(iter)
        self.assertEqual(d.gmin, [1, 2, 2])
        self.assertEqual(d.heap, [(5, 2, 2), (7, 2, 0)])


def __starting_point():

    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    print(calculate())


__starting_point()
