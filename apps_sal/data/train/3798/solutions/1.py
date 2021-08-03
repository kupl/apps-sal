from collections import Counter


def cards_and_pero(s):
    return [13 - s.count(c) for c in 'PKHT'] if max(Counter([(s[i * 3:i * 3 + 3]) for i in range(len(s) // 3)]).values()) <= 1 else [-1, -1, -1, -1]
