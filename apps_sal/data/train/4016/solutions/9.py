def game(a, b):
    if a * b == 0:
        return "Non-drinkers can't play"
    m, j = 0, 0
    i = 1
    while(True):
        if i % 2 == 1:
            m += i
            if m > a:
                return "Joe"
        else:
            j += i
            if j > b:
                return "Mike"
        i += 1
