from math import log2

ns=["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

def get_note(p):
    return ns[round(log2(p/55)*12)%12]
