def jumping_number(number):
    number = str(number)
    for i in range(len(number) - 1):
        if abs(int(number[i + 1]) - int(number[i])) != 1:
            return 'Not!!'
    return 'Jumping!!'
