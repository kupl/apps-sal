keys = {1: "A", 2: "A#", 3: "B", 4: "C", 5: "C#", 6: "D", 7: "D#", 8: "E", 9: "F", 10: "F#", 11: "G", 12: "G#", }


def which_note(n):

    return keys.get(((n - 1) % 88 % 12) + 1)
