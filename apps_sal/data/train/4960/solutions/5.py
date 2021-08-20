class Harshad(object):
    harshad = [n for n in range(1, 12534) if n % sum((int(d) for d in str(n))) == 0]

    @staticmethod
    def is_valid(number):
        return number in Harshad.harshad

    @staticmethod
    def get_next(number):
        return next((n for n in Harshad.harshad if n > number))

    @staticmethod
    def get_series(count, start=0):
        i = Harshad.harshad.index(Harshad.get_next(start))
        return Harshad.harshad[i:i + count]
