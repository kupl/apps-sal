class Multiples:

    def __init__(self, maximum):
        self.maximum = maximum

    def sum(self, base):
        count = self.maximum // base + 1
        last = base * (count - 1)
        return count * last // 2


def solution(number):
    multiples = Multiples(number - 1)
    return multiples.sum(3) + multiples.sum(5) - multiples.sum(15)
