base = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}


def minor_or_major(c):
    return 'Not a chord' if sum((n in base for n in c.split())) != 3 else (lambda ns: 'Major' if (12 + base[ns[1]] - base[ns[0]]) % 12 == 4 and (12 + base[ns[2]] - base[ns[1]]) % 12 == 3 else 'Minor' if (12 + base[ns[1]] - base[ns[0]]) % 12 == 3 and (12 + base[ns[2]] - base[ns[1]]) % 12 == 4 else 'Not a chord')(c.split())
