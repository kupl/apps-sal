def interpreter(code, tape):
    t = list(map(int, tape))
    position = address = depth = 0
    while -1 < position < len(tape) and address < len(code):
        if depth:
            depth += code[address] is "["
            depth -= code[address] is "]"
        else:
            t[position] ^= code[address] is "*"
            depth += code[address] is "[" and not t[position]
            depth -= code[address] is "]" and t[position]
            position += code[address] is ">"
            position -= code[address] is "<"
        address += 1 - 2 * (depth < 0)
    return "".join(map(str, t))
