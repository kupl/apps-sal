def parse_float(string):
    lst = []
    if type(lst)==type(string):
        return None
    elif("a"<=string[0]>="z")or("A"<=string[0]>="A"):
        return None
    else:
        return float(string)

