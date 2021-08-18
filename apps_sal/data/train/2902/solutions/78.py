def opposite(number):
    string = str(number)
    if string[0] == "-":
        return float(string[1:])
    else:
        return float("".join(["-", string]))
