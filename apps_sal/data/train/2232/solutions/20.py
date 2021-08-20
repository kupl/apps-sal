"""
upsolving:
brute forcing takes too long
parlay congruence relation
"""
import math
n = int(input())
zs = 2
for lvl in range(1, n + 1):
    print(((lvl * (lvl + 1)) ** 2 - zs) // lvl)
    zs = lvl * (lvl + 1)
