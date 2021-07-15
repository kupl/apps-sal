def jumping_number(n):
    s = str(n)
    return ['Not!!', 'Jumping!!'] [all(abs(int(d1)-int(d2))==1 for d1, d2 in zip(s[:-1], s[1:]))]
