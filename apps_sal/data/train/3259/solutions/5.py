from collections import namedtuple


def tv_remote(word: str):
    remote = ('a', 'b', 'c', 'd', 'e', '1', '2', '3', 'f', 'g', 'h', 'i', 'j', '4', '5', '6', 'k', 'l', 'm', 'n', 'o', '7', '8', '9', 'p', 'q', 'r', 's', 't', '.', '@', '0', 'u', 'v', 'w', 'x', 'y', 'z', '_', '/', '', ' ')
    Position = namedtuple('Position', 'y x')
    (shift, shift_pressed) = (Position(5, 0), False)
    prev = Position(0, 0)
    button_presses = 0
    for letter in word:
        if letter.isalpha() and letter.isupper() != shift_pressed:
            button_presses += abs(prev.y - shift.y) + abs(prev.x - shift.x) + 1
            (prev, shift_pressed) = (shift, not shift_pressed)
        cur = Position(*divmod(remote.index(letter.lower()), 8))
        button_presses += abs(prev.y - cur.y) + abs(prev.x - cur.x) + 1
        prev = cur
    return button_presses
