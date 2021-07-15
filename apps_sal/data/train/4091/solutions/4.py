ks = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
keys = ks * 7 + ks[:4]

def which_note(n):
    return keys[(n - 1) % len(keys)]
