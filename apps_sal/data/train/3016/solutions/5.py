def minor_or_major(chord):
    interval = {'C': 1, 'C#': 2, 'Db': 2, 'D': 3, 'D#': 4, 'Eb': 4, 'E': 5, 'F': 6, 'F#': 7, 'Gb': 7, 'G': 8, 'G#': 9, 'Ab': 9, 'A': 10, 'A#': 11, 'Bb': 11, 'B': 12}
    chord = chord.split()
    if len([i for i in chord if i in interval]) == 3:
        if interval[chord[1]] - interval[chord[0]] in [4, -8] and interval[chord[2]] - interval[chord[1]] in [3, -9]:
            return 'Major'
        elif interval[chord[1]] - interval[chord[0]] in [3, -9] and interval[chord[2]] - interval[chord[1]] in [4, -8]:
            return 'Minor'
        else:
            return 'Not a chord'
    else:
        return 'Not a chord'
