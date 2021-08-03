from fractions import gcd


def para_to_rect(*equations):
    changes = [(" ", ""), ("-t", "-1t"), ("=t", "=+1t"),
               ("+t", "+1t"), ("x=", ""), ("y=", "")]
    equationsR = []
    for equation in equations:
        for (s1, s2) in changes:
            equation = equation.replace(s1, s2)
        equationsR += equation.split("t")
    a, b, c, d = [int(n) for n in equationsR]
    e, f, g = c, -a, b * c - a * d
    h = gcd(gcd(e, f), g)
    e, f, g = e // h, f // h, g // h
    if e < 0:
        e, f, g = -e, -f, -g
    ysign = "+"
    if f < 0:
        ysign, f = "-", -f
    return "{}x {} {}y = {}".format(e if abs(e) > 1 else "-" if e == -1 else "",
                                    ysign, f if f > 1 else "", g)
