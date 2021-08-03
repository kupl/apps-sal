def smallest(n):
    previous = 1
    for i in range(1, n + 1):
        previous = mmc(previous, i)  # mmc stands for least common multiple
        previous = int(previous)  # the mmc function returns float
    return previous


def mmc(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto is not 0:
        resto = a % b
        a = b
        b = resto

    return (num1 * num2) / a
