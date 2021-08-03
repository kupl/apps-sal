def which_note(key_press_count):
    return ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"][(key_press_count - 1) % 88 % 12]
