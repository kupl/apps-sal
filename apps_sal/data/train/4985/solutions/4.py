def transpose(song, interval):
    sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    result = []
    
    for note in song:
        if note in sharp:
            result.append(sharp[(sharp.index(note) + interval) % 12])
        else:
            result.append(sharp[(flat.index(note) + interval) % 12])
    
    return result
