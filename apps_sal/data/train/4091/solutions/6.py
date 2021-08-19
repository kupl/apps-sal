def which_note(n):
    return 'A A# B C C# D D# E F F# G G#'.split()[~-n % 88 % 12]
