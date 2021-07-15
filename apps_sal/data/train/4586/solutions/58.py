def tv_remote(word):
    keyboard = [
        ['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
        ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
        ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
        ['p', 'q', 'r', 's', 't', '.', '@', '0'],
        ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']
    ]
    x, y = 0, 0
    count = 0
    for char in word:
        for i in range(len(keyboard)):
            if char in keyboard[i]:
                y2 = i
                x2 = keyboard[i].index(char)
                count += 1 + abs(y2 - y) + abs(x2 - x)
                x, y = x2, y2
    return count
