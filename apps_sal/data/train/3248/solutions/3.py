notesDictionary = {
    440: "A",
    466.16: "A
    493.88: "B",
    523.25: "C",
    554.37: "C
    587.33: "D",
    622.25: "D
    659.25: "E",
    698.46: "F",
    739.99: "F
    783.99: "G",
    830.61: "G
}


def get_note(pitch):
    for key, value in notesDictionary.items():
        if max(pitch, key) % min(pitch, key) == 0:
            return value
