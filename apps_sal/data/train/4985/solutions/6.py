def transpose(s, i):
    return (lambda sharp, flat: [sharp[(flat.index(n) + i + 12) % 12] if n in flat else sharp[(sharp.index(n) + i + 12) % 12] for n in s])(['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'], ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'])
