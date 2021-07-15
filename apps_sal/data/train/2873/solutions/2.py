import sys
# Set new (higher) recursion limit
sys.setrecursionlimit(int(1e6))

# Source: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
# (I couldn't come up with the formula myself :p)
josephus_survivor = lambda n, k: 1 if n == 1 else ((josephus_survivor(n - 1, k) + k - 1) % n) + 1
