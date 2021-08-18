table = "A Bb B C Db D Eb E F Gb G Ab".split()
table += "A A


def transpose(song, interval):
    return [table[table.index(note) + interval % 12 + 12] for note in song]
