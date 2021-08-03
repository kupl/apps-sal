def expanded_form(num):
    s = str(num)
    n = len(s)
    return ' + '.join([s[-i] + "0" * (i - 1) for i in range(n, 0, -1) if s[-i] != "0"])
