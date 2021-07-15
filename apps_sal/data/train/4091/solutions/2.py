NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NUMBER_OF_KEYS = 88

def which_note(key_press_count):
    return NOTES[(key_press_count - 1) % NUMBER_OF_KEYS % len(NOTES)]

