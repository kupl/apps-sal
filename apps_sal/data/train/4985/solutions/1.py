table = 'A Bb B C Db D Eb E F Gb G Ab'.split()
table += 'A A# B C C# D D# E F F# G G#'.split() * 3


def transpose(song, interval):
    return [table[table.index(note) + interval % 12 + 12] for note in song]
