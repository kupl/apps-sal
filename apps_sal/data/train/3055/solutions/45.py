def sum_str(a, b):
    if b == "" and a != "":
        return str(a)
    if a == "" and b != "":
        return str(b)
    if a != "" and b != "":
        a1 = int(float(a))
        b1 = int(float(b))
        return str(a1 + b1)
    else:
        return '0'
