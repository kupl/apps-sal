def sum_digits(number):
    digits = []
    remove = []
    num_sum = 0
    if number < 0:
        number = abs(number)
    for split in str(number):
        digits.append(split)
    print(digits)
    for add in digits:
        num_sum += int(add)
    print(num_sum)
    return num_sum
