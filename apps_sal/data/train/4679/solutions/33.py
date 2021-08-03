from re import sub


def to_freud(sentence: str) -> str:
    """ Replace every word in the sentece by `sex`. """
    return sub("\S+", "sex", sentence)
