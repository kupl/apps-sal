def sum_str(a, b):
    if a == " " and b == " ":
        return "0"
    elif a == " ":
        return b
    elif b == " ":
        return a
    elif a == "9" or b == "9":
        return "9"
    else:
        try:
            c = str(int(a) + int(b))
            return c
        except ValueError:
            return "0"
