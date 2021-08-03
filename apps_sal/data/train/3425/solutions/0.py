from collections import Counter


def word_square(ls):
    n = int(len(ls)**0.5)
    return n * n == len(ls) and sum(i % 2 for i in list(Counter(ls).values())) <= n
