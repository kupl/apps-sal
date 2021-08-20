from difflib import get_close_matches
import sys
import os


def closeMatches(patterns, word):
    return get_close_matches(word, patterns, 1, 0.9)[0]


def get_string():
    return sys.stdin.readline().strip()


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


ans = []
test = int(input())
for i in range(test):
    (n, q) = get_ints()
    n = int(n)
    q = int(q)
    patterns = []
    for j in range(n):
        s = get_string()
        patterns.append(s)
    for j in range(q):
        word = get_string()
        ans.append(closeMatches(patterns, word))
for j in ans:
    sys.stdout.write(j + '\n')
