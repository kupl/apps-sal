from collections import Counter

def char_freq(message):
    return dict(Counter(list(message)))
