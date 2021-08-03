def sum_digits(number):
    total = 0
    for num in str(abs(number)):
        total += int(str(num))

    return total


print(sum_digits(23))
