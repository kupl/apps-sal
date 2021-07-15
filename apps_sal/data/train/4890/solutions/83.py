from numpy import prod as vol
def find_difference(a, b):
    return abs(vol(a)-vol(b))
