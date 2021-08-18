def transpose(song, interval):
    altern = {"Bb": "A
    notes = ['A', 'A
    return [notes[(notes.index(altern.get(i, i)) + interval) % 12] for i in song]
