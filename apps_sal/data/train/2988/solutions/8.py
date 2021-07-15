from itertools import zip_longest

def reverse_and_combine_text(text):
    L = text.split()
    if len(L) == 1: return text
    return reverse_and_combine_text(' '.join(x[::-1] + y[::-1] for x,y in zip_longest(L[::2], L[1::2], fillvalue='')))
