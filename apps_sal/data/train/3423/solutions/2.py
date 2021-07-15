from itertools import combinations

def solve(arr, n):
    return any(sum(xs) % n == 0
               for i in range(len(arr))
               for xs in combinations(arr, i+1))
