"""
Code Chef :: December 2020 Lunchtime :: Even Sequence Problem Code: EVSTR
https://www.codechef.com/LTIME91B/problems/EVSTR
"""
import sys
from math import inf


def solve(A):
 dp = [-inf for _ in range(len(A)+1)]
 dp[0] = 0
 for i, a in enumerate(A):
  even = dp[0]
  odd = dp[a]
  dp[a] = max(dp[a], even + 1)
  dp[0] = max(dp[0], odd + 1)

 return len(A) - dp[0]


def main():
 """Main program."""
 test_cases = int(sys.stdin.readline())
 for _ in range(test_cases):
  N = int(sys.stdin.readline())
  A = [int(i) for i in sys.stdin.readline().split()]
  soln = solve(A)
  print(soln)


def __starting_point():
 main()

__starting_point()
