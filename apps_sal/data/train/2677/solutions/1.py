from collections import namedtuple

Position = namedtuple('Position', 'y x')


def tv_remote(word: str):
    remote = (
        'a', 'b', 'c', 'd', 'e', '1', '2', '3',
        'f', 'g', 'h', 'i', 'j', '4', '5', '6',
        'k', 'l', 'm', 'n', 'o', '7', '8', '9',
        'p', 'q', 'r', 's', 't', '.', '@', '0',
        'u', 'v', 'w', 'x', 'y', 'z', '_', '/',
        '', ' '
    )
    shift, shift_pressed = Position(5, 0), False

    prev = Position(0, 0)
    button_presses = 0
    for letter in word:
        if letter.isalpha() and letter.isupper() != shift_pressed:
            button_presses += calc_presses(prev, shift)
            prev, shift_pressed = shift, not shift_pressed

        cur = Position(*divmod(remote.index(letter.lower()), 8))
        button_presses += calc_presses(prev, cur)
        prev = cur

    return button_presses


def calc_presses(pos1: Position, pos2: Position):
    dif_y, dif_x = abs(pos1.y - pos2.y), abs(pos1.x - pos2.x)
    return min(dif_y, 6 - dif_y) + min(dif_x, 8 - dif_x) + 1
