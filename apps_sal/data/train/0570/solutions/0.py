from collections import deque, defaultdict
from math import sqrt, ceil, factorial
import sys
import copy
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):

    s = input()
    if len(s) > 6:
        ans = 0
        rem = len(s) - 6
        ans += factorial(len(s))
        ans -= 2 * (factorial(len(s) - 2))
        ans += factorial(rem + 2)
        print(ans)

    else:
        if 'k' in s and 'r' in s and 'a' in s and 's' in s and 'h' in s and 'i' in s:
            ans = 0
            rem = len(s) - 6
            ans += factorial(len(s))
            ans -= 2 * (factorial(len(s) - 2))
            ans += factorial(rem + 2)
            print(ans)
        else:
            if 'k' in s and 'a' in s and 'r' in s:
                ans = 0
                rem = len(s) - 3
                ans += factorial(len(s))
                ans -= factorial(rem + 1)
                print(ans)
                continue
            if 's' in s and 'h' in s and 'i' in s:
                ans = 0
                rem = len(s) - 3
                ans += factorial(len(s))
                ans -= factorial(rem + 1)
                print(ans)
                continue

            print(factorial(len(s)))
