def solution(number):
    def s(m):
        n = (number - 1) // m
        return n * m * (n + 1) // 2
    return s(3) + s(5) - s(15)
