# generate the first ~2000 elements
from bisect import bisect
HARSHAD = [n for n in range(1, 13000) if n % sum(map(int, str(n))) == 0]


class Harshad:
    @staticmethod
    def is_valid(n):
        return n in HARSHAD

    @staticmethod
    def get_next(n):
        return HARSHAD[bisect(HARSHAD, n)]

    @staticmethod
    def get_series(cnt, n=0):
        start = bisect(HARSHAD, n)
        return HARSHAD[start: start + cnt]
