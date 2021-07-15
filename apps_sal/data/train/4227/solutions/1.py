def complexSum(arr):
    a = [complex(i.replace("i", "j")) for i in arr]
    s = 0
    for i in a:
        s += i
    if s == 1j:
        return "i"
    elif s == -1j:
        return "-i"
    elif s.imag == 0j:
        s = int(s.real)
    s = str(s).replace("j", "i").lstrip("(").rstrip(")")
    return s
