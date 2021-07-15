def berserk_rater(synopsis):
    n = sum([score(s.upper()) for s in synopsis])
    return 'worstest episode ever' if n < 0 else 'bestest episode ever' if n > 10 else str(n)
    
def score(s):
    return 5 if 'CLANG' in s else -2 if 'CG' in s else -1
