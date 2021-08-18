keys = {1: "A", 2: "A


def which_note(n):

    return keys.get(((n - 1) % 88 % 12) + 1)
