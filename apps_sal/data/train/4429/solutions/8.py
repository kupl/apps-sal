from collections import Counter


def longest_palindrome(s):
    flag = res = 0
    for v in Counter(map(str.lower, filter(str.isalnum, s))).values():
        flag |= v & 1
        res += v >> 1 << 1
    return res + flag
