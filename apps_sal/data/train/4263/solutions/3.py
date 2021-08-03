import re


def apparently(stg):
    return re.sub(r"\b(and|but)\b(?! apparently\b)", r"\1 apparently", stg)
