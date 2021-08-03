from itertools import islice


def solution(digits):
    return int(max(map(''.join, zip(*(islice(digits, a, None) for a in range(5))))))
