def jumping_number(number):
    s = str(number)
    l = len(s)
    return 'Jumping!!' if sum([1 for x in range(1, l) if abs(int(s[x - 1]) - int(s[x])) == 1]) == l - 1 else 'Not!!'
