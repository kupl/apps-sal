def automorphic(n):
    a = n * n
    b = list(str(a))
    c = list(str(n))
    if len(c) == 1:
        if b[-1] == c[-1]:
            return "Automorphic"
        else:
            return "Not!!"
    elif len(c) == 2:
        if b[-1] == c[-1] and b[-2] == c[-2]:
            return "Automorphic"
        else:
            return "Not!!"
    elif len(c) == 3:
        if b[-1] == c[-1] and b[-2] == c[-2] and b[-3] == c[-3]:
            return "Automorphic"
        else:
            return "Not!!"
    elif len(c) == 4:
        if b[-1] == c[-1] and b[-2] == c[-2] and b[-3] == c[-3] and b[-4] == c[-4]:
            return "Automorphic"
        else:
            return "Not!!"
    elif len(c) == 5:
        if b[-1] == c[-1] and b[-2] == c[-2] and b[-3] == c[-3] and b[-4] == c[-4] and b[-4] == c[-4]:
            return "Automorphic"
        else:
            return "Not!!"
