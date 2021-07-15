def minimum(arr):
    mi=100000
    for a in arr:
        if a<mi:
            mi=a
    return mi
def maximum(arr):
    ma=-1000000
    for b in arr:
        if b>ma:
            ma=b
    return ma
