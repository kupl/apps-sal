from re import sub

def to_freud(sentence: str) -> str:
    """ Replace every word in the sentece by `sex`. """
    return sub(r"\b[\w\'']+\b", "sex", sentence)
