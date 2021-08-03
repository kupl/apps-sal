class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum(map(int, str(number))) == 0

    @staticmethod
    def get_next(number):
        n = number + 1
        while not Harshad.is_valid(n):
            n += 1
        return n

    @staticmethod
    def get_series(count, start=0):
        result = [Harshad.get_next(start)]
        for _ in range(count - 1):
            result.append(Harshad.get_next(result[-1]))
        return result
