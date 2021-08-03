import datetime


def elapsed_seconds(start, end):
    diff = end - start
    return diff.total_seconds()
