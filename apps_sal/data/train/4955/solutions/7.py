from functools import reduce

def ride(group,comet):
    score = lambda name : reduce(lambda x, y: x*y, map(lambda c : ord(c) - 64, name) ) % 47 
    return ["STAY", "GO"][score(group) == score(comet)]
