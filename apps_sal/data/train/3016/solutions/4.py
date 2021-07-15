NOTES = {'C':0, 'C#':1, 'Db':1, 'D':2, 'D#':3, 'Eb':3, 'E':4, 'F':5, 'F#':6, 'Gb':6, 'G':7, 'G#':8, 'Ab':8, 'A':9, 'A#':10, 'Bb':10, 'B':11 }
def minor_or_major(chord):
    notes = chord.split(' ')
    if len(notes) != 3 : return 'Not a chord'
    first,second,third = [NOTES[note] if note in NOTES else 0 for note in notes]
    interval = (second-first+12)%12
    return 'Not a chord' if (third-first+12)%12 != 7 or interval not in (3,4) else 'Minor' if interval==3 else 'Major'
