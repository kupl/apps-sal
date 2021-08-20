import sys
sys.setrecursionlimit(int(1000000.0))


def josephus_survivor(n, k):
    return 1 if n == 1 else (josephus_survivor(n - 1, k) + k - 1) % n + 1
