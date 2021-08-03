def parse(data):
    value = 0
    res = []
    for c in data:
        if c == "i":
            value += 1
        elif c == "d":
            value -= 1
        elif c == "s":
            value *= value
        elif c == "o":
            res.append(value)
    return res
