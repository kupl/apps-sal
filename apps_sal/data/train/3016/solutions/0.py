from itertools import product

NOTES =  [['C'], ['C#', 'Db'], ['D'], ['D#', 'Eb'], ['E'], ['F'], ['F#', 'Gb'], ['G'], ['G#', 'Ab'], ['A'], ['A#', 'Bb'], ['B']]*2
config = [('Major', 4), ('Minor', 3)]

DCT_CHORDS = {c: mode for mode, offset in config
                      for i in range(len(NOTES)//2)
                      for c in product(NOTES[i], NOTES[i + offset], NOTES[i + 7])}

def minor_or_major(chord):
    chord = tuple(chord.split()) if isinstance(chord, str) else ""
    return DCT_CHORDS.get(chord, "Not a chord")
