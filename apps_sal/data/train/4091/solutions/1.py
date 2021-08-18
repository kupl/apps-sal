keyboard = "A A


def which_note(count):
    return keyboard[(count - 1) % 88 % 12]
