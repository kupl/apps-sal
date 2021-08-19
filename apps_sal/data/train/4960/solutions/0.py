from itertools import count, islice


class Harshad:

    @staticmethod
    def is_valid(number):
        return number % sum(map(int, str(number))) == 0

    @classmethod
    def get_next(cls, number):
        return next((i for i in count(number + 1) if cls.is_valid(i)))

    @classmethod
    def get_series(cls, c, start=0):
        return list(islice(filter(cls.is_valid, (i for i in count(start + 1))), c))
