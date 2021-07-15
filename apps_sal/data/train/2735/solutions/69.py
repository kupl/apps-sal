def jumping_number(number):
    s = int(str(number)[0]) - 1
    if len(str(number)) > 1:
        for i in str(number):
            if s + 1 == int(i) or s - 1 == int(i):
                s = int(i)
                continue
            else:
                return "Not!!"

    return "Jumping!!"
