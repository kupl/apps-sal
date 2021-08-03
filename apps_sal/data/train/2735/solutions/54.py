def jumping_number(number):
    if number < 11:
        return "Jumping!!"
    else:
        prev = int(str(number)[0])
        for i, x in enumerate(str(number)[1:]):
            if prev - int(x) == 1 or prev - int(x) == -1:
                prev = int(x)
            else:
                return "Not!!"
        return "Jumping!!"
