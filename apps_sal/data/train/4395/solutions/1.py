from itertools import count
def next_higher(value):
    bits = bin(value).count('1')
    return next(i for i in count(value+1) if bin(i).count('1')==bits)
