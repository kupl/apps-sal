def sum_digits(number):
    num = str(number)
    num = [int(x) for x in num if x != '-']
    return sum(num)
