from itertools import count, islice
D = {}


class Harshad:

    @staticmethod
    def is_valid(number):
        return D.get(number, D.setdefault(number, not number % sum(map(int, str(number)))))

    @staticmethod
    def get_next(number):
        return next(filter(Harshad.is_valid, count(number + 1)))

    @staticmethod
    def get_series(size, start=0):
        return list(islice(filter(Harshad.is_valid, count(start + 1)), size))
