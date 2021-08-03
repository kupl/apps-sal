from itertools import count


def palindrome(num):
    return next(c for b in count(0) for c in (num + b, num - b) if c > 9 and c == int(str(c)[::-1])) if isinstance(num, int) and num >= 0 else 'Not valid'
