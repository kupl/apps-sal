def minor_or_major(chord):

    interval = {"C": 1, 'C
                'F

    chord = chord.split()

    if len([i for i in chord if i in interval]) == 3:
        if interval[chord[1]] - interval[chord[0]] in [4, -8] and interval[chord[2]] - interval[chord[1]] in [3, -9]:
            return "Major"

        elif interval[chord[1]] - interval[chord[0]] in [3, -9] and interval[chord[2]] - interval[chord[1]] in [4, -8]:
            return "Minor"

        else:
            return "Not a chord"
    else:
        return "Not a chord"
