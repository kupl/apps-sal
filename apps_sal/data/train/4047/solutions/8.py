table = str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72")


def to_leet_speak(stg):
    return stg.translate(table)
