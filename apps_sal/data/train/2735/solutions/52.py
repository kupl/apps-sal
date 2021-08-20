def jumping_number(number):
    s = str(number)
    if len(s) < 2:
        return 'Jumping!!'
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 1:
            return 'Not!!'
    return 'Jumping!!'
