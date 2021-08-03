def parse(data):
    def process_char(c):
        nonlocal v
        if c == "i":
            v += 1
        elif c == "d":
            v -= 1
        elif c == "s":
            v *= v
        elif c == "o":
            return True

    v = 0
    return [v for c in data if process_char(c)]
