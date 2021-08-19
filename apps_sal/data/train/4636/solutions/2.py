from collections import namedtuple
from itertools import repeat, cycle

Position = namedtuple('Position', 'y x')
shift = Position(5, 0)

remote = (
    (
        'a', 'b', 'c', 'd', 'e', '1', '2', '3',
        'f', 'g', 'h', 'i', 'j', '4', '5', '6',
        'k', 'l', 'm', 'n', 'o', '7', '8', '9',
        'p', 'q', 'r', 's', 't', '.', '@', '0',
        'u', 'v', 'w', 'x', 'y', 'z', '_', '/',
        '', ' '
    ),
    (
        'A', 'B', 'C', 'D', 'E', '1', '2', '3',
        'F', 'G', 'H', 'I', 'J', '4', '5', '6',
        'K', 'L', 'M', 'N', 'O', '7', '8', '9',
        'P', 'Q', 'R', 'S', 'T', '.', '@', '0',
        'U', 'V', 'W', 'X', 'Y', 'Z', '_', '/',
        '', ' '
    ),
    (
        '^', '~', '?', '!', "'", '"', '(', ')',
        '-', ':', ';', '+', '&', '%', '*', '=',
        '<', '>', '€', '£', '$', '¥', '¤', '\\',
        '[', ']', '{', '}', ',', '.', '@', '§',
        '#', '¿', '¡', '', '', '', '_', '/',
        '', ' '
    )
)


def tv_remote(word: str):
    modes = cycle(remote)
    prev, mode, button_presses = Position(0, 0), next(modes), 0

    for letter in word:
        try:
            i = mode.index(letter)

        except ValueError:
            button_presses += calc_presses(prev, shift)
            mode = next(modes)
            prev = shift

            try:
                i = mode.index(letter)

            except ValueError:
                button_presses += 1
                mode = next(modes)
                i = mode.index(letter)

        cur = Position(*divmod(i, 8))
        button_presses += calc_presses(prev, cur)
        prev = cur

    return button_presses


def calc_presses(pos1: Position, pos2: Position):
    dif_y, dif_x = abs(pos1.y - pos2.y), abs(pos1.x - pos2.x)
    return min(dif_y, 6 - dif_y) + min(dif_x, 8 - dif_x) + 1
