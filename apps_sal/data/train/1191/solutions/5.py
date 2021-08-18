from difflib import get_close_matches
import sys


def closeMatches(patterns, word):
    print(get_close_matches(word, patterns, 1, 0.8)[0])


def get_string():
    return sys.stdin.readline().strip()


test = int(input())
for i in range(test):
    n, q = input().split(" ")
    n = int(n)
    q = int(q)
    patterns = []
    for i in range(n):
        s = get_string()
        patterns.append(s)
    for i in range(q):
        word = get_string()
        closeMatches(patterns, word)
