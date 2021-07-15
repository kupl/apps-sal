def which_note(key_press_count):
    key_press_count = key_press_count % 88 - 1
    L = ["A", "A#", "B"] + ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]*7 + ["C"]
    return L[key_press_count]

