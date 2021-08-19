def permutation_average(n):
    digits = [int(i) for i in str(n)]
    length = len(str(n))

    def factorial(n):
        if n is 1 or n is 0:
            return 1
        else:
            return n * factorial(n - 1)

    averager = factorial(length)  # denominator of the average

    def get_coefficient(width):  # after adding up all the digits, a pattern is seen dependent on
        coefficient = 0  # the number of digits there are. This exploits that
        if width <= 1:
            coefficient = 1
        else:
            for x in range(width):
                coefficient += factorial(width - 1) * (10**x)

        return coefficient

    total = 0
    for index in digits:  # just multiplying the same coefficient (ironically enough) with every digit
        multiplier = get_coefficient(length)
        total += multiplier * index

    average = total / float(averager)
    avg = int(round(average, 0))
    return avg
