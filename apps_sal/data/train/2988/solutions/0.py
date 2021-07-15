from itertools import zip_longest

def reverse_and_combine_text(text):
    words = text.split(' ')
    while len(words) > 1:
        it = map(lambda w: w[::-1], words)
        words = [a + b for a, b in zip_longest(it, it, fillvalue='')]
    return words[0]
