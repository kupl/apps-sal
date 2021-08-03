from itertools import cycle


def encode(message, key):
    letters = []
    fullkey = [int(x) for x in str(key)]
    for character in message:
        number = ord(character) - 96
        letters.append(number)
    outcome = [x + y for x, y in zip(letters, cycle(fullkey),)]
    return outcome
