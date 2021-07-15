def sum_digits(number):
    count = 0
    number = abs(number)
    for num in str(number):
        count = count + int(num)
    return (count)
    # ...

