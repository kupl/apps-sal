from typing import Tuple

KEYBOARDS = [
    [
        'abcde123',
        'fghij456',
        'klmno789',
        'pqrst.@0',
        'uvwxyz_/',
    ],
    [
        'ABCDE123',
        'FGHIJ456',
        'KLMNO789',
        'PQRST.@0',
        'UVWXYZ_/',
    ],
    [
        '^~?!\'\"()',
        '-:;+&%*=',
        '<>€£$¥¤\\',
        '[]{},.@§',
        '#¿¡   _/',
    ],
]

Position = Tuple[int, int]

SPACE = 5, 1
SWITCH_MODE = 5, 0


def get_pos(mode: int, c: str) -> Position:
    if c == ' ':
        return SPACE

    for i, chars in enumerate(KEYBOARDS[mode]):
        if c in chars:
            return i, chars.index(c)


def get_diff(a: Position, b: Position) -> int:
    (x1, y1), (x2, y2) = a, b
    x, y = abs(x1 - x2), abs(y1 - y2)
    return min(x, 6 - x) + min(y, 8 - y)


def mode_switch(mode: int, c: str, pos: Position) -> Tuple[int, int, Position]:
    if c == ' ' or c in ''.join(KEYBOARDS[mode]):
        return mode, 0, pos

    switches = get_diff(pos, SWITCH_MODE)
    while c not in ''.join(KEYBOARDS[mode]):
        switches += 1
        mode = (mode + 1) % len(KEYBOARDS)

    return mode, switches, SWITCH_MODE


def tv_remote(words: str):
    total = mode = 0
    pos = 0, 0
    for w in words:
        mode, switches, pos = mode_switch(mode, w, pos)
        new_pos = get_pos(mode, w)
        total += switches + get_diff(pos, new_pos) + 1
        pos = new_pos

    return total
