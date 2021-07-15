def sum_str(a, b):

    if not a and not b:
        return '0'
    elif b == "":
        return a
    elif a == "":
        return b       
    else:
        a = int(a)
        b = int(b)
        return str(a + b)
