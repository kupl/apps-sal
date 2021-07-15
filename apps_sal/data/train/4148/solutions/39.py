def sum_digits(number):
    result = 0
    for num in str(number):
        try:
            result += int(num)
        except:
            continue
    return result
