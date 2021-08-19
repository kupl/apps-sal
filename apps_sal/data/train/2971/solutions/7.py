import numpy as np


def watch_pyramid_from_the_side(characters):
    return characters and '\n'.join(((i + i * level * 2).center(len(characters) * 2 - 1) for (level, i) in enumerate(characters[::-1]))) or characters


def watch_pyramid_from_above(characters):

    def to_char(x):
        return chr(x)
    int_to_char = np.vectorize(to_char)
    try:
        arr = np.asarray([ord(characters[-1])])[np.newaxis]
        for i in characters[::-1][1:]:
            arr = np.pad(arr, pad_width=1, mode='constant', constant_values=ord(i))
        return '\n'.join(map(''.join, int_to_char(arr).tolist()))
    except (TypeError, IndexError):
        return characters


def count_visible_characters_of_the_pyramid(characters):
    return characters and (len(characters) * 2 - 1) ** 2 or -1


def count_all_characters_of_the_pyramid(characters):
    return characters and sum(((1 + level * 2) ** 2 for (level, _) in enumerate(characters))) or -1
