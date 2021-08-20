import re


def solution(stones):
    return sum((len(m[0]) - 1 for m in re.finditer('(.)\\1+', stones)))
