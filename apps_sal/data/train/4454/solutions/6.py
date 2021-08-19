def presses(phrase):
    return sum(map(int, phrase.upper().translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ *#1234567890', '123123123123123123412312341111444445452'))))
