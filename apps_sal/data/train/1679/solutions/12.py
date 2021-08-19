"""

    Author - AYUSHMAN CHAHAR #

"""

import bisect
import math
import heapq
import itertools
import sys
#import numpy
from itertools import combinations
from itertools import permutations
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(10000000)

if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream

if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""

        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.

    Args:
        sync (bool, optional): The new synchronization setting.

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        def input(): return sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def main():

    for _ in range(int(eval(input()))):
        n, length, xored = list(map(int, input().split()))
        ans = [-1] * n
        templ = [0] * (length - 1)
        templ.append(xored)
        # print(templ)
        temp = n % length
        for i in range(len(templ)):
            templ.append(templ[i])
        start = 0
        for i in range(len(ans)):
            ans[i] += (templ[start] + 1)
            # print(ans)
            # print(templ[start])
            start += 1
            if start == len(templ):
                start = 0
        print(*ans)


def __starting_point():
    sync_with_stdio(False)
    main()


__starting_point()
