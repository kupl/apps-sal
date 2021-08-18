def which_note(key_press_count):
    piano = ("A", "A
             "A", "A
             "A", "A
             "A", "A
             "A", "A
             "A", "A
             "A", "A
             "A", "A

    return piano[key_press_count % 88 - 1]
