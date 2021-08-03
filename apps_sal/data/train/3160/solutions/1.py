import functools


def multi(l_st):
    return functools.reduce(lambda x, y: x * y, l_st)


def add(l_st):
    return functools.reduce(lambda x, y: x + y, l_st)


def reverse(string):
    return string[::-1]
