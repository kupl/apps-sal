import sys


def args_count(*argv, **kwargs):
    count = 0
    for i in argv:
        count += 1
    for i in kwargs:
        count += 1
    return count
