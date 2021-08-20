def jumping_number(number):
    number = str(number)
    for i in range(1, len(number)):
        if abs(int(number[i - 1]) - int(number[i])) != 1:
            return 'Not!!'
    return 'Jumping!!'
