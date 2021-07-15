def jumping_number(number):
    s = str(number)
    return next(('Not!!' for a,b in zip(s, s[1:]) if abs(int(b)-int(a)) != 1), 'Jumping!!')
