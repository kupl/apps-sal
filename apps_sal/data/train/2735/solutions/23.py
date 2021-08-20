def jumping_number(number):
    if len(str(number)) == 1:
        return 'Jumping!!'
    else:
        number = str(number)
        for n in range(1, len(number)):
            if abs(int(number[n]) - int(number[n - 1])) != 1:
                return 'Not!!'
        return 'Jumping!!'
