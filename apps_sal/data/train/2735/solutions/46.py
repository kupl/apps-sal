def jumping_number(number):
    j=int(str(number)[0])
    for i in str(number)[1:]:
        if int(i)-j in (1,-1):
            j=int(i)
        else:
            return 'Not!!'
    return 'Jumping!!'
