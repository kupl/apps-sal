def jumping_number(number):
    nstr = str(number)
    return 'Jumping!!' if all(abs(int(a) - int(b)) == 1 for a, b in zip(nstr, nstr[1:])) else 'Not!!'
