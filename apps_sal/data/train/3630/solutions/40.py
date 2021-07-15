def arithmetic(a, b, operator):
    while operator[0] == "a":
        return a + b
        break
    while operator[0] == "s":
        return a - b
        break
    while operator[0] == "m":
        return a * b
        break
    else:
        return a / b

