def check_root(string):
    try:
        a, b, c, d = [int(i) for i in string.split(',')]
        if not (a == b - 1 and a == c - 2 and a == d - 3):
            return 'not consecutive'
        s = a * b * c * d + 1
        return str(s) + ', ' + str(int(s**0.5))
    except:
        return 'incorrect input'
