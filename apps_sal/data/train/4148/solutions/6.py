def sum_digits(number):
    return sum((int(ele) for ele in str(abs(number))))
