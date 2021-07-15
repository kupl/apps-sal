def analyse(x):
    n = (b := bin(x)).rstrip("0")
    p = len(b) - len(n)
    return  (n := int(n, 2)) == 1, p * (-1)**(n == 1), n


def sharkovsky(a, b):
    return analyse(a) < analyse(b)
