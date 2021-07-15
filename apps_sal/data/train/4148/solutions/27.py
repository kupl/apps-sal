def sum_digits(number):
    result = 0
    is_minus = False
    
    if (number < 0):
        is_minus = True
        number = number * -1
    for element in str(number):
        result += int(element)
    
    return result
