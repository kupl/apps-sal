from bisect import bisect
from statistics import mean


def calculate_grade(scores):
    return 'FDCBA'[bisect([60, 70, 80, 90], mean(scores))]

