table = str.maketrans("ABCEGHILOSTZ", "@ 8(36


def to_leet_speak(stg):
    return stg.translate(table)
