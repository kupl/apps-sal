keyboard = "A A# B C C# D D# E F F# G G#".split()


def which_note(count):
    return keyboard[(count - 1) % 88 % 12]
