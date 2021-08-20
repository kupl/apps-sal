"""
 _____   _    _   __    __     ____     __    _
/ ____| | |  | | |  \\  /  |   /    \\   |  \\  | |
| |___  | |  | | |   \\/   |  /   _  \\  | . \\ | |
\\____ \\ | |  | | | |\\__/| | |   /_\\  | | |\\ \\| |
____| | | \\__/ | | |    | | |   __   | | | \\ ` |
|_____/ \\______/ |_|    |_| |__|  |__| |_|  \\__|

"""
from math import cos, acos, tan, atan, atan2, sin, asin, radians, degrees, hypot
from math import pi, sqrt, gcd, ceil, floor, log2, log10, factorial
from sys import stdin, stdout, stderr, setrecursionlimit
from functools import reduce
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from statistics import mean, median, mode
from collections import deque, OrderedDict, defaultdict
from re import compile, findall, escape, search, match
from bisect import insort, insort_left, insort_right, bisect_left, bisect_right, bisect
from random import choice, getrandbits, randint, random, randrange, shuffle
from collections import Counter, namedtuple, ChainMap, UserDict, UserList, UserString
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge, nlargest, nsmallest
from numpy import dot, trace, argmax, argmin, array, cumprod, cumsum, matmul
'\n/*\nTemplate by Sai Suman Chitturi\nLinkedin: https://www.linkedin.com/in/sai-suman-chitturi-9727a2196/\nHackerrank: https://www.hackerrank.com/skynetasspyder?hr_r=1\nCodechef: https://www.codechef.com/users/suman_18733097\nCodeforces: http://codeforces.com/profile/saisumanchitturi\nGithub: https://github.com/ChitturiSaiSuman\nHackerearth: https://www.hackerearth.com/@chitturi7\nSPOJ: Sai Suman Chitturi @out_of_bound\n*/\n'
mod = 10 ** 9 + 7
hell = 10 ** 9 + 9
inf = 10 ** 18


def lcm(x, y):
    return x * y // gcd(x, y)


def add(x, y):
    return (x % mod + y % mod) % mod


def sub(x, y):
    return (x % mod - y % mod + mod) % mod


def mul(x, y):
    return x % mod * (y % mod) % mod


def inverse(x):
    return pow(x, mod - 2, mod)


def setBitCount(x):
    return bin(x).count('1')


def sumOfDigits(x):
    return sum([int(i) for i in str(x)])


size = 10 ** 6 + 1
setrecursionlimit(size)


def preCompute():
    return


def solve():
    return


def main():
    io = IO()
    testcases = 0
    if testcases == 0:
        testcases = io.nextInt()
    preCompute()
    for test in range(testcases):
        s = io.String()
        n = len(s)
        ans = 0
        for i in range(n // 2):
            ans += abs(ord(s[i]) - ord(s[n - i - 1]))
        io.write(ans)


class IO:

    def next(self):
        return stdin.readline().strip()

    def nextLine(self):
        return self.next()

    def String(self):
        return self.next()

    def nextStrings(self):
        return list(map(str, self.next().split()))

    def nextInt(self):
        return int(self.next())

    def Int(self):
        return self.nextInt()

    def nextFloat(self):
        return float(next())

    def Float(self):
        return self.nextFloat()

    def nextList(self):
        return list(map(int, self.next().split()))

    def List(self):
        return self.nextList()

    def nextTuple(self):
        return tuple(map(int, self.next().split()))

    def Tuple(self):
        return self.nextTuple()

    def debug(self, *obj, sep=' ', end='\n'):
        string = sep.join([str(item) for item in obj]) + end
        stderr.write(string)

    def print(self, *obj, sep=' ', end='\n'):
        string = sep.join([str(item) for item in obj]) + end
        stdout.write(string)

    def write(self, *obj, sep=' ', end='\n'):
        self.print(*obj, sep=sep, end=end)


main()
