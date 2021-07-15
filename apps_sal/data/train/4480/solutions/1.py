def parse(data):
    arr = []
    value = 0
    for c in data:
        if c == "i":
            value += 1
        elif c == "d":
            value -= 1
        elif c == "s":
            value = value**2
        elif c == "o":
            arr.append(value)
    return arr
