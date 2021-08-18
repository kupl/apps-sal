def permutation_average(n):
    digits = [int(i) for i in str(n)]
    length = len(str(n))

    def factorial(n):
        if n is 1 or n is 0:
            return 1
        else:
            return n * factorial(n - 1)

    averager = factorial(length)

    def get_coefficient(width):
        coefficient = 0
        if width <= 1:
            coefficient = 1
        else:
            for x in range(width):
                coefficient += factorial(width - 1) * (10**x)

        return coefficient

    total = 0
    for index in digits:
        multiplier = get_coefficient(length)
        total += multiplier * index

    average = total / float(averager)
    avg = int(round(average, 0))
    return avg
