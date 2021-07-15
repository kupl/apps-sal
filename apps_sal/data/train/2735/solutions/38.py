def jumping_number(number):
    st = str(number)
    if len(st) == 1:
        return "Jumping!!"
    for i,c in enumerate(st):
        if i == 0:
            continue
        if int(c) != int(st[i-1]) + 1:
            if int(c) != int(st[i-1]) - 1:
                return "Not!!"
        
    return "Jumping!!"

