def asterisc_it(n):
    if type(n) == list:
        n = "".join(str(i) for i in n)
    if type(n) == int:
        n = str(n)
    return "".join([a + "*" if int(a) % 2 == 0 and int(b) % 2 == 0 else a for a, b in zip(n, n[1:])]) + n[-1]
