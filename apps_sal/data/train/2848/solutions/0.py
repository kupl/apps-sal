from itertools import combinations_with_replacement

def find(arr,n):
    return sum( sum(c) == n for x in range(1,len(arr)+1) for c in combinations_with_replacement(arr, x) )
