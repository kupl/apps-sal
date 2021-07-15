class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        from itertools import combinations
        l = list(combinations(arr, 3))
        res = []
        for tup in l:
            if  abs(tup[0] - tup[1]) <= a and abs(tup[0] - tup[2]) <= c and abs(tup[2] - tup[1]) <= b:
                res.append(tup)
                
        return len(res)
        

