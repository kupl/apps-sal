def jumping_number(number):
    if len(str(number)) > 1:
        jumping = True
        for i in range(1, len(str(number))):
            if not abs(int(str(number)[i]) - int(str(number)[i - 1])) == 1:
                jumping = False
    else:
        jumping = True
    if jumping:
        return 'Jumping!!'
    else:
        return 'Not!!'
