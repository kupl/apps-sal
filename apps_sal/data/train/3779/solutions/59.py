def past(h, m, s):
    a = (h * 60 + m) * 60
    return (a + s) * 1000
