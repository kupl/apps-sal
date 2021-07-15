from operator import itemgetter

def sort_time(arr):
    L = sorted(arr, key=itemgetter(0))
    result = [L.pop(0)]
    while L:
        result.append(L.pop(next((i for i in range(len(L)) if L[i][0] >= result[-1][1]), 0)))
    return result
