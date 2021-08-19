def tv_remote(word):
    keyboard = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', 'f', 'g', 'h', 'i', 'j', '4', '5', '6', 'k', 'l', 'm', 'n', 'o', '7', '8', '9', 'p', 'q', 'r', 's', 't', '.', '@', '0', 'u', 'v', 'w', 'x', 'y', 'z', '_', '/']
    (prev_y, prev_x) = (0, 0)
    strokes = 0
    for char in word:
        (x, y) = (keyboard.index(char) % 8, keyboard.index(char) // 8)
        dist = abs(prev_x - x) + abs(prev_y - y) + 1
        (prev_x, prev_y) = (x, y)
        strokes += dist
    return strokes
