def capitalize(s):
    evens = []
    g = 0
    for char in s:
        if g % 2 == 0:
            evens.append(char.title())
        else:
            evens.append(char)
        g += 1
    odds = [x.swapcase() for x in evens]
    return [''.join(evens), ''.join(odds)]
