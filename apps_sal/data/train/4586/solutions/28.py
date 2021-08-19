def tv_remote(word):
    screen_keyboard_layout = [['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']]
    screen_keyboard_symbols = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    if not all([ch in screen_keyboard_symbols for ch in word]):
        return -1
    button_presses = 0
    (cur_position, next_position) = ((0, 0), (0, 0))
    for ch in word:
        for (i, row) in enumerate(screen_keyboard_layout):
            if ch in row:
                next_position = (i, row.index(ch))
        button_presses += abs(next_position[0] - cur_position[0]) + abs(next_position[1] - cur_position[1]) + 1
        cur_position = next_position
    return button_presses
