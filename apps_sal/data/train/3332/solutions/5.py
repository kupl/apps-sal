import re


def autocorrect(i):
    return " ".join(re.sub(r"^(y+o+u+|u)([,.!])?$", r"your sister\2", word, flags=re.IGNORECASE) for word in i.split())
