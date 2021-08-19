from collections import Counter
from string import ascii_letters, digits


def longest_palindrome(data):
    cnt = Counter([d for d in data.lower() if d in ascii_letters + digits])
    even = sum([n for n in list(cnt.values()) if n % 2 == 0])
    odd = sorted([n for n in list(cnt.values()) if n % 2 != 0])[::-1]
    if len(odd) == 0:
        ans = even
    if len(odd) == 1:
        ans = even + odd[0]
    if len(odd) > 1:
        ans = even + odd[0] + sum([n - 1 for n in odd[1:]])
    return ans
