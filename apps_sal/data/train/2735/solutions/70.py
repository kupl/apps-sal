def jumping_number(number):
    number = str(number)
    if len(number) == 1:
        return 'Jumping!!'
    for i in range(1, len(number)):
        if abs(int(number[i]) - int(number[i - 1])) != 1:
            return 'Not!!'
    return 'Jumping!!'
