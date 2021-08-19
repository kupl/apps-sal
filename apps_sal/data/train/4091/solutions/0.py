def which_note(count):
    return 'A A# B C C# D D# E F F# G G#'.split()[(count - 1) % 88 % 12]
