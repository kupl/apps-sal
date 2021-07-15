def last(x):
    a = x.split()
    last_char = []
    i = 0
    for word in a:
        last_char.append((word[-1], i, word))
        i = i + 1
    last_char = sorted(last_char)
    output = [word for char, i, word in last_char]
    return output
