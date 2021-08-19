def jumping_number(number):
    prev = number % 10
    number //= 10
    while number:
        digit = number % 10
        if abs(prev - digit) != 1:
            return 'Not!!'
        prev = digit
        number //= 10
    return 'Jumping!!'
