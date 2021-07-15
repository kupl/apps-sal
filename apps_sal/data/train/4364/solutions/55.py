def odd_or_even(arr):
    s=sum(arr)
    o="odd"
    e="even"
    if len(arr)>0:
        if s%2==1:
            return o
        else:
            return e
    else:
        return o

