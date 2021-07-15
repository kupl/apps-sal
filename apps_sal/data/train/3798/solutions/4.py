from collections import  Counter

def cards_and_pero(s):
    xs = [s[i:i+3] for i in range(0, len(s), 3)]
    if len(xs) != len(set(xs)):
        return [-1, -1, -1, -1]
    suit = Counter(s[::3])
    return [13-suit[c] for c in 'PKHT']
