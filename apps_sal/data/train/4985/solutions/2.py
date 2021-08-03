SHARP = "A, A#, B, C, C#, D, D#, E, F, F#, G, G#".split(", ")
FLAT = "A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab".split(", ")
REVERSED_INDEX = {**{note: i for i, note in enumerate(SHARP)},
                  **{note: i for i, note in enumerate(FLAT)}}


def transpose(song, interval):
    return [SHARP[(REVERSED_INDEX[note] + interval) % 12] for note in song]
