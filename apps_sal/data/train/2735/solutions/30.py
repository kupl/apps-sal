def jumping_number(number):
    s = str(number)
    return 'Jumping!!' if all(abs(int(x) - int(y)) == 1 for x, y in zip(s[:-1], s[1:])) else 'Not!!'
