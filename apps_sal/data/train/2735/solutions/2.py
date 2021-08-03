def jumping_number(number):
    digits = [int(n) for n in list(str(number))]
    for i in range(len(digits) - 1):
        if abs(digits[i] - digits[i + 1]) != 1:
            return 'Not!!'
    return 'Jumping!!'
