from itertools import count, takewhile

def word_mesh(arr):
    overlaps = list(takewhile(bool, map(mesher, zip(arr,arr[1:])) ))
    return len(overlaps)==len(arr)-1 and ''.join(overlaps) or 'failed to mesh'
    
def mesher(pair):
    a, b   = pair
    nChars = next( i for i in count(min(map(len,pair)),-1)
                     if a.endswith(b[:i]) )
    return b[:nChars]
