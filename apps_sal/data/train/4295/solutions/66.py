def balanced_num(number):
    n = str(number)
    length = len(n)
    b = sum(int(x) for x in n[:(length - 1) // 2]) == sum(int(x) for x in n[(length + 2) // 2:])
    string = "" if b else "Not "
    return f"{string}Balanced"
