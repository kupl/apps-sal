from collections import Counter


def word_square(letters):
    n = len(letters) ** 0.5
    if n != int(n):
        return False
    n = int(n)
    c = Counter(letters)
    (one, odd) = (0, 0)
    for i in c.values():
        if i == 1:
            one += 1
            odd += 1
        elif i != 1 and i % 2 != 0:
            odd += 1
    if one > n or odd > n:
        return False
    else:
        return True
