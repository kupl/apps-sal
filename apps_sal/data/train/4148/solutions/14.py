def sum_digits(number):
    return sum(int(i) if not i=='-' else 0 for i in str(number))
