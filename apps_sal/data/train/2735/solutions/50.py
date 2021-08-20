def jumping_number(n):
    if n < 0:
        return 'Not!!'
    s = str(n)
    if len(s) == 1:
        return 'Jumping!!'
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 1:
            return 'Not!!'
    else:
        return 'Jumping!!'
