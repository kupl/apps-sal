def word_square(s):
    return len(s) ** 0.5 % 1 == 0 and sum((s.count(c) % 2 for c in set(s))) <= len(s) ** 0.5
