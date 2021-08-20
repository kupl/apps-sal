def check_root(string):
    try:
        (a, b, c, d) = map(int, string.split(','))
        if a + 3 == b + 2 == c + 1 == d:
            x = a + (a + 1) ** 2
            return '{}, {}'.format(x ** 2, abs(x))
        return 'not consecutive'
    except:
        return 'incorrect input'
