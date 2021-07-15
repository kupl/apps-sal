from itertools import combinations
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        comb = combinations(range(len(arr)), 3)
        condition = lambda i, j, k: i < j and j < k and abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c
        return len([(i, j, k) for (i, j, k) in comb if condition(i, j, k)])
