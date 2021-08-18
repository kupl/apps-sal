def make_negative(number):
    if(number > 0):
        return int("-{}".format(number))
    elif number == 0:
        return 0
    else:
        return number
