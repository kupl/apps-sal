def jumping_number(number):
    print(number)
    if number < 10:
        return "Jumping!!"
    for k,v in enumerate(str(number)):
        if k == 0:
            if int(v) - int(str(number)[k+1]) in [1, -1]:
                pass
            else:
                return "Not!!"
        elif k == len(str(number)) - 1:
            if int(v) - int(str(number)[k-1]) in [1, -1]:
                pass
            else:
                return "Not!!"
        else:
            if int(v) - int(str(number)[k+1]) in [1, -1] and int(v) - int(str(number)[k+1]) in [1, -1]:
                pass
            else:
                return "Not!!"
    return "Jumping!!"

