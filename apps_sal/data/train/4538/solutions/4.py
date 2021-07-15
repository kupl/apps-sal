from itertools import zip_longest

def merge(sequences, fillvalue=None):
    for slice in zip_longest(*sequences, fillvalue=fillvalue):
        for item in slice:
            yield item

def reverse_fun(text):
    mid = len(text) // 2
    return ''.join(merge((text[:mid-1:-1], text[:mid]), fillvalue=''))

