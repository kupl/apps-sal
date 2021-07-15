from itertools import zip_longest

def number_of_carries(a, b):
    x, y = str(a)[::-1], str(b)[::-1]
    result = c = 0
    for a, b in zip_longest(map(int, x), map(int, y), fillvalue=0):
        c = (a + b + c) > 9
        result += c
    return result
