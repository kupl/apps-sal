import re


def rm(word):
    left = len(re.search('^!*', word).group())
    right = len(re.search('!*$', word).group())
    ex = '!' * min(left, right)
    return ex + word.strip('!') + ex


def remove(s):
    return ' '.join(map(rm, s.split()))
