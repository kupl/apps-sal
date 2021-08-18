def presses(phrase):
    return sum(map(int, phrase.upper().translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ *
