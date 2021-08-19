d = {'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'}
q = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']


def transpose(a, n):
    return [q[(q.index(d.get(x, x)) + n) % len(q)] for x in a]
