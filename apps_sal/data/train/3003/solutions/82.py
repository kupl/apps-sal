import sys


def args_count(*args, **kwargs):
    i = 0
    for num in args:
        i += 1
    for key in kwargs.items():
        i += 1
    return i
