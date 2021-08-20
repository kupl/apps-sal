def jumping_number(number):
    s = str(number)
    return ('Not!!', 'Jumping!!')[all((0 for (a, b) in zip(s, s[1:]) if abs(int(b) - int(a)) != 1))]
