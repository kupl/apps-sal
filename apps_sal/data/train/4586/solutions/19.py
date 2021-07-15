def tv_remote(word: str):
    remote = (
        'a', 'b', 'c', 'd', 'e', '1', '2', '3',
        'f', 'g', 'h', 'i', 'j', '4', '5', '6',
        'k', 'l', 'm', 'n', 'o', '7', '8', '9',
        'p', 'q', 'r', 's', 't', '.', '@', '0',
        'u', 'v', 'w', 'x', 'y', 'z', '_', '/'
    )

    button_presses = prev_y = prev_x = 0
    for letter in word:
        y, x = divmod(remote.index(letter), 8)
        button_presses += abs(prev_y - y) + abs(prev_x - x) + 1
        prev_y, prev_x = y, x

    return button_presses
