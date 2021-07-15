def sum_digits(number):
    n = str(abs(number))
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum
