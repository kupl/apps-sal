def triple_trouble(one, two, three):
    s = one + two + three
    A = len(s)
    B = len(one)
    answ = ""
    start = 0
    for j in range(B):
        for i in range(start, A, B):
            answ += s[i]
        start += 1
    return answ
