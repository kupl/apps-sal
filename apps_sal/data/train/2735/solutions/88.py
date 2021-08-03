def jumping_number(number):
    s = str(number)
    return 'Not!!' if any(abs(int(s[i - 1]) - int(s[i])) != 1 for i in range(1, len(s))) else 'Jumping!!'
