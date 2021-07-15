trans = "abcdefghijklmnopqrstuvwxyz" * 2
trans += trans.upper() + "0123456789" * 2

def ROT135(input):
    output = []
    for c in input:
        if c.isalpha():
            c = trans[trans.index(c) + 13]
        elif c.isdigit():
            c = trans[trans.index(c) + 5]
        output.append(c)
    return "".join(output)
