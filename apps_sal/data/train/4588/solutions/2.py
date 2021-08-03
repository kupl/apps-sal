def controller(s):
    current, pause, door, output, i = 0, 0, 0, [], 0
    for symbol in s:
        if symbol == 'P':
            if pause:
                pause = False
            elif not door and not current:
                door = True
            elif door and current == 5:
                door = False
            else:
                pause = True
        elif symbol == 'O':
            door ^= 1
        current += [[[0, -1][current > 0], [0, 1][current < 5]][door], 0][pause]
        output.append(str(current))
    return ''.join(output)
