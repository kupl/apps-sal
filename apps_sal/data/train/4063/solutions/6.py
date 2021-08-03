import re


def evenator(s):
    return " ".join([w if len(w) % 2 == 0 else w + w[-1] for w in re.sub(r'[!_.?,]', "", s).split()])
