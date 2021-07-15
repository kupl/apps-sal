def transpose(song, interval):
    sharp="A A# B C C# D D# E F F# G G#".split()
    flat="A Bb B C Db D Eb E F Gb G Ab".split()
    return [sharp[((sharp.index(note) if note in sharp else flat.index(note))+12+interval)%12] for note in song]
