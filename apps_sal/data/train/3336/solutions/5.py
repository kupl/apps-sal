def get_sum_of_digits(num):
    digits = []
    for i in str(num):
        digits.append(int(i))
    return sum(digits)
