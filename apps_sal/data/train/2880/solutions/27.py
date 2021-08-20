def seven(m, n=0):
    return len(str(m)) > 2 and seven(int(int(str(m)[:-1]) - 2 * int(str(m)[-1])), -~n) or (m, n)
