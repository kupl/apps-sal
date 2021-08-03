import itertools


def reverse_in_parentheses(string):
    stream = iter(string)
    return _recurse(stream)


def safe_rev(s):
    return s[::-1].translate(str.maketrans('()', ')('))


def _recurse(stream):
    ret = ''
    for c in stream:
        if c == '(':
            ret += c
            ret += safe_rev(_recurse(stream)) + ')'
        elif c == ')':
            break
        else:
            ret += c
    return ret
