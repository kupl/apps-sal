# a*b*c*d + 1
# = a*(a+1)*(a+2)*(a+3) + 1
# = a**4 + 6*a**3 + 11*a**2 + 6*a + 1
# = (a**2 + 3*a + 1)**2
# = (a**2 + 2*a + 1 + a)**2
# = ((a+1)**2 + a)**2
# sqtr = (a+1)**2 + a

def check_root(string):
    try:
        a, b, c, d = map(int, string.split(','))
        if a + 3 == b + 2 == c + 1 == d:
            x = a + (a + 1)**2
            return "{}, {}".format(x**2, abs(x))
        return "not consecutive"
    except:
        return "incorrect input"
