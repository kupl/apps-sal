def binRota(arr):
    return list(office(arr))
    
def office(arr):
    w = 0
    for e in arr:
        yield from e[::[1,-1][w]]
        w = not w
