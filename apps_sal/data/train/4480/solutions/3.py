COMMANDS = {
    'i': lambda x: x + 1,
    'd': lambda x: x - 1,
    's': lambda x: x * x,
}

def parse(data):
    result, x = [], 0
    for c in data:
        if c == 'o':
            result.append(x)
        elif c in COMMANDS:
            x = COMMANDS[c](x)
    return result
