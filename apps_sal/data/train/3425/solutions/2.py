from collections import Counter

def word_square(letters):
    N = len(letters)**0.5
    return not N%1 and (sum(v&1 for v in Counter(letters).values()) <= N)
