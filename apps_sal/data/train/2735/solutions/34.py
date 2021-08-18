def jumping_number(number):

    for i in range(1, len(str(number))):
        if abs(int(str(number)[i]) - int(str(number)[i - 1])) != 1:
            return 'Not!!'

    return 'Jumping!!'
