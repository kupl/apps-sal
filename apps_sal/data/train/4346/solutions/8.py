a = '"a" - 6 "b" - 1 "d" - 7 "e" - 4 "i" - 3 "l" - 2 "m" - 9 "n" - 8 "o" - 0 "t" - 5'
d = {k: v for (v, k) in __import__('re').findall('\\"(\\w)\\"\\s-\\s(\\d)', a)}


def hidden(n):
    return ''.join((d.get(x, '') for x in str(n)))
