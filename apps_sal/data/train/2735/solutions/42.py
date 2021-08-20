def jumping_number(number):
    s = str(number)
    print(s)
    for (n, i) in enumerate(s[1:]):
        l = int(s[n])
        i = int(i)
        if abs(l - i) != 1:
            return 'Not!!'
        else:
            continue
    return 'Jumping!!'
