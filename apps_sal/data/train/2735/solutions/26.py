def jumping_number(number):
    number = [int(i) for i in str(number)]
    for i in range(len(number) - 1):
        if not abs(number[i] - number[i + 1]) == 1:
            return 'Not!!'
    return 'Jumping!!'
