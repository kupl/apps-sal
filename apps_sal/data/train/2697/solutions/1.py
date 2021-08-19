import re


def solution(s):
    return re.sub('([A-Z])', ' \\1', s)
