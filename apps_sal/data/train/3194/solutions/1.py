import re

CG = re.compile(r"\bcg\b", flags=re.I)
CLANG = re.compile(r"\bclang", flags=re.I)


def berserk_rater(synopsis):
    score = sum(
        (5 if CLANG.search(line) else (-2 if CG.search(line) else -1))
        for line in synopsis
    )
    return (
        "worstest episode ever"
        if score < 0
        else "bestest episode ever"
        if score > 10
        else str(score)
    )
