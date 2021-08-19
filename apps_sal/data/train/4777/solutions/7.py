from collections import Counter


def check(s, t):
    return not s or any((check(s[d:], t - {d}) for d in range(max(map(len, t)) + 1) if s[:d] in t))


def mystery_range(s, n):
    for i in range(1, 100):
        t = Counter(''.join(map(str, range(i, i + n))))
        if Counter(s) == Counter(t):
            return [i, i + n - 1] if check(s, set(map(str, range(i, i + n)))) else [i + 1, i + n]
