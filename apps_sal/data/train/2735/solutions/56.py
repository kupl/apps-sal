def jumping_number(number):
    n = str(number)
    c = 0
    if len(n) == 1:
        return 'Jumping!!'
    for i in range(len(n) - 1):
        if (int(n[i + 1]) == int(n[i]) + 1 or int(n[i + 1]) == int(n[i]) - 1):
            c += 1
    if c == len(n) - 1:
        return 'Jumping!!'
    return 'Not!!'
