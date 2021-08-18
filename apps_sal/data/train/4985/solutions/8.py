sharp = ['A', 'A
flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']


def transpose(song, interval):
    return [sharp[((sharp.index(note) if note in sharp else flat.index(note)) + interval) % 12] for note in song]
