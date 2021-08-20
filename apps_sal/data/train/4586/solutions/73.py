import string


def tv_remote(word):
    let = 0
    numbers = '123456789.@0z_/'
    keyboard = {(i, j): 0 for i in range(1, 6) for j in range(1, 9)}
    for i in range(1, 6):
        for j in range(1, 6):
            keyboard[i, j] = string.ascii_lowercase[let]
            let += 1
    let = 0
    for i in range(1, 6):
        for j in range(6, 9):
            keyboard[i, j] = numbers[let]
            let += 1
    print(keyboard)
    keys = list(keyboard.keys())
    vals = list(keyboard.values())
    cursor = [1, 1]
    moves = 0
    for i in word:
        moves += 1 + (abs(keys[vals.index(i)][0] - cursor[0]) + abs(keys[vals.index(i)][1] - cursor[1]))
        cursor = keys[vals.index(i)]
    return moves
