def jumping_number(number):
    x = str(number)
    if len(str(number)) == 1:
           return 'Jumping!!'
    else:
        for i in range(len(x)-1):
            if abs(int(x[i]) - int(x[i+1])) == 1:
                continue
            else:
                return 'Not!!'
        return 'Jumping!!'
