from itertools import product

NOTES = [['C'], ['C#', 'Db'], ['D'], ['D#', 'Eb'], ['E'], ['F'], ['F#', 'Gb'], ['G'], ['G#', 'Ab'],
         ['A'], ['A#', 'Bb'], ['B']] * 2
MAJOR = set(c for i in range(len(NOTES) // 2) for c in product(NOTES[i], NOTES[i + 4], NOTES[i + 7]))
MINOR = set(c for i in range(len(NOTES) // 2) for c in product(NOTES[i], NOTES[i + 3], NOTES[i + 7]))


def minor_or_major(chord):
    chord = tuple(chord.split()) if isinstance(chord, str) else ("", "", "")
    return "Major" if chord in MAJOR else "Minor" if chord in MINOR else "Not a chord"
