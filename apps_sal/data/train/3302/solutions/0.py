from itertools import combinations
def strings_crossover(arr, result):
    return sum(1 for s1,s2 in combinations(arr,2) if all(r in (x,y) for x,y,r in zip(s1,s2,result)))
