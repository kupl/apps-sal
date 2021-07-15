def transpose(song, interval):
    sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    return [sharp[(12 + (sharp.index(nt) if nt in sharp else flat.index(nt)) + interval) % 12] for nt in song]
