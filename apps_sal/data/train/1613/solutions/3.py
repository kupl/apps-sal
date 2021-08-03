import re


def solution(string, markers):
    for marker in markers:
        string = re.sub(r' *?\{}.*$'.format(marker), '', string, flags=re.M)
    return string
