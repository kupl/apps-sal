"""
Codeforces Contest 260 Div 1 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


def main():
    n, k = read()
    s = set()
    for i in range(n):
        s.add(read(0))
    s = list(s)
    s.sort()
    s = treeify(s)
    res = solve(s)
    if res == 0:
        print("Second")
    if res == 1:
        print("First" if k % 2 else "Second")
    if res == 2:
        print("Second")
    if res == 3:
        print("First")


def treeify(s):
    res = [[] for _ in range(26)]
    for i in s:
        if i:
            res[ord(i[0]) - 97].append(i[1:])
    fin = []
    for i in range(26):
        if res[i]:
            fin.append(treeify(res[i]))
    return fin


def solve(s, parity=2):
    for i in range(len(s)):
        if isinstance(s[i], list):
            s[i] = solve(s[i], 3 - parity)
    if not s:
        return parity
    if 0 in s:
        return 3
    if 1 in s and 2 in s:
        return 3
    if 1 in s:
        return 1
    if 2 in s:
        return 2
    return 0


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return map(int, inputs.split())


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


main()
