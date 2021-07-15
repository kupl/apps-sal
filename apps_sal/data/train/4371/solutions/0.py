from itertools import combinations

def digits(num):
    return list(map(sum, combinations(map(int,str(num)),2)))
