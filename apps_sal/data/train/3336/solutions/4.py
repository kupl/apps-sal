def get_sum_of_digits(num):
    sum = int()
    digits = str(num)
    for x in digits:
        sum += int(x)
    return sum
