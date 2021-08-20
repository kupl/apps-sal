from collections import Counter


def sabb(s, value, happiness):
    C = Counter(s.lower())
    score = value + happiness + sum((C[c] for c in set('sabbatical')))
    return 'Sabbatical! Boom!' if score > 22 else 'Back to your desk, boy.'
