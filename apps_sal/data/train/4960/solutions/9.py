class Harshad:
    @staticmethod
    def is_valid(number):
        if number == 0:
            return False
        sumdigits = sum(int(d) for d in str(number))
        return number % sumdigits == 0

    @staticmethod
    def get_next(number):
        while True:
            number += 1
            if Harshad.is_valid(number):
                return number

    @staticmethod
    def get_series(count, start=0):
        answer = []
        for _ in range(count):
            start = Harshad.get_next(start)
            answer.append(start)
        return answer
