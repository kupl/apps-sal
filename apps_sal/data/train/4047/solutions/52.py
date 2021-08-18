def to_leet_speak(str):
    trans = str.maketrans('ABCEGHILOSTZ', '@ 8(36
    return str.translate(trans)
