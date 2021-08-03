from itertools import zip_longest


def reverse_and_combine_text(text):
    ws = text.split()
    while len(ws) > 1:
        ws = [w1[::-1] + w2[::-1] for w1, w2 in zip_longest(*[iter(ws)] * 2, fillvalue='')]
    return ws[0]
