def tv_remote(word):
    keypad = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
              ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
              ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
              ['p', 'q', 'r', 's', 't', '.', '@', '0'],
              ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    sum = 0
    coords = [(0, 0)]
    for char in list(word):
        for index, row in enumerate(keypad):
            if char in row:
                coords.append((index, row.index(char)))
    for c, point in enumerate(coords, 0):
        if c == 0:
            continue
        a, b = point
        sum += abs(coords[c][0] - coords[c - 1][0])
        sum += abs(coords[c][1] - coords[c - 1][1])
        sum += 1
        print(sum)
    return sum
