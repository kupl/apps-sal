def jumping_number(number):
    number = str(number)
    jumping = True
    for i in range(1, len(number)):
        if int(number[i]) - int(number[i - 1]) in [-1, 1]:
            continue
        else:
            jumping = False
    return "Jumping!!" if jumping else "Not!!"
