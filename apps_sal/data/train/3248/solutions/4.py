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


def adjust_pitch(pitch):
    if pitch in notesDictionary:
        return pitch
    elif pitch < 440:
        while pitch not in notesDictionary:
            pitch *= 2
        return pitch
    elif pitch > 830:
        while pitch not in notesDictionary:
            pitch = pitch / 2
        return pitch
    else:
        return -1


def get_note(pitch):
    return notesDictionary[adjust_pitch(pitch)]
