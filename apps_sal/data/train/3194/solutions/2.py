from functools import reduce
def berserk_rater(s): return (lambda score: "worstest episode ever" if score < 0 else "bestest episode ever" if score > 10 else str(score))(reduce(lambda a, b: a + (lambda b: 5 if "clang" in b else -2 if "cg" in b else -1)(b.lower()), s, 0))
