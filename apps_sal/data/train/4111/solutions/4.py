from collections import Counter


def sabb(s, value, happiness):
    cnt = Counter(s.lower())
    return ("Back to your desk, boy.", "Sabbatical! Boom!")[sum(cnt[a] for a in set('sabbatical')) + value + happiness > 22]
