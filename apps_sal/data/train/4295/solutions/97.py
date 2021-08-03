def balanced_num(number):
    number = str(number)
    a = len(number)
    hm1 = number[:int((a / 2) - 1)]
    hm2 = number[int((a // 2) + 1):]
    hm3 = number[:int((a // 2) + 1)]
    hm4 = number[int((a // 2)):]
    print
    if a == 1:
        return "Balanced"
    elif a % 2 == 0:
        if sum(int(x) for x in hm1) == sum(int(y) for y in hm2):
            return "Balanced"
        else:
            return "Not Balanced"
    elif a % 2 != 0:
        if sum(int(w) for w in hm3) == sum(int(z) for z in hm4):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        return "Not Balanced"
