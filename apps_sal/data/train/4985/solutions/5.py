def transpose(song, interval):
    notes = ["A", "A
             "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    return [notes[(12 + notes.index(n) + interval) % 12] for n in song]
