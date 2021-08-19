def sum_digits(number):
    k = sum(list(map(int, str(abs(number)))))
    return k
