NOTES = {'C': 0, 'C


def minor_or_major(chord):
    notes = chord.split(' ')
    if len(notes) != 3:
        return 'Not a chord'
    first, second, third = [NOTES[note] if note in NOTES else 0 for note in notes]
    interval = (second - first + 12) % 12
    return 'Not a chord' if (third - first + 12) % 12 != 7 or interval not in (3, 4) else 'Minor' if interval == 3 else 'Major'
