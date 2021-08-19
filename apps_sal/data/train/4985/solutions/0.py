def transpose(song, interval):
    altern = {'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'}
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    return [notes[(notes.index(altern.get(i, i)) + interval) % 12] for i in song]
