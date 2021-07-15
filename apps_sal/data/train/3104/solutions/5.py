from math import ceil

# Why is this 6 kyu?
def reindeer(presents):
    if presents > 180: raise Exception("Too many presents")
    return 2 + ceil(presents/30)
