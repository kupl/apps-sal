def how_many_dalmatians(n):
    if n <= 10:
        return 'Hardly any'
    elif 10 < n <= 50:
        return 'More than a handful!'
    elif 50 < n < 101:
        return "Woah that's a lot of dogs!"
    elif n == 101:
        return '101 DALMATIONS!!!'
