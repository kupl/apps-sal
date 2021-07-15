def sum_digits(number):
    numberList = [int(x) for x in str(abs(number))]
    return sum(numberList)
