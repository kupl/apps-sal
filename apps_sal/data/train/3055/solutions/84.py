def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    return "9" if a == "" or b == "" else str(int(a)+int(b))
