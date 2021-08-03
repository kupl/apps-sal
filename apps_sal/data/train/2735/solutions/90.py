def jumping_number(number):
    number = str(number)
    for i in range(len(number) - 1):
        if (int(number[i]) - int(number[i + 1]))**2 != 1:
            return 'Not!!'
    return 'Jumping!!'
