def parse(data):
    curr = 0
    output = []
    for cmd in data:
        if cmd == "i":
            curr += 1
        elif cmd == "d":
            curr -= 1
        elif cmd == "s":
            curr *= curr
        elif cmd == "o":
            output.append(curr)
    return output
