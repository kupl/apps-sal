from bisect import bisect_right


class Harshad:
    values, values_set = [], set()
    i = 1
    while len(values) < 2000:
        if not i % sum(int(x) for x in str(i)):
            values.append(i)
            values_set.add(i)
        i += 1

    @staticmethod
    def is_valid(n):
        return n in Harshad.values_set

    @staticmethod
    def get_next(n):
        return Harshad.values[bisect_right(Harshad.values, n)]

    @staticmethod
    def get_series(n, s=0):
        x = bisect_right(Harshad.values, s)
        return Harshad.values[x:x + n]
