def find_difference(a, b):
    def mul(li):
        car = 1
        for i in li:
            car *= i
        return car
    return abs(mul(a) - mul(b))
