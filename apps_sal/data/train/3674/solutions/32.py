def add_binary(a, b):
    c = a + b
    output = []
    while c / 2 != 0:
        output.append(str(c % 2))
        c = c // 2
    output.reverse()
    return ''.join(output)
