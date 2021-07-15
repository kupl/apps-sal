from collections import defaultdict

def char_freq(message):
    res = defaultdict(int)
    for c in message:
        res[c] += 1
    return res
