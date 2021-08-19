"""
Codeforces Round 254 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


# SOLUTION
n, m = read()
v = read()
best = 0
for i in range(m):
    a, b, c = read()
    temp = (v[a - 1] + v[b - 1]) / c
    best = max(best, temp)
print(best)
