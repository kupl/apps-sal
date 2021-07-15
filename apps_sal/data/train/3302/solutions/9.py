from itertools import combinations

def strings_crossover(arr, result):
    return sum(1 for a,b in combinations(arr,2) if all(r in (x,y) for r,x,y in zip(result,a,b)))

