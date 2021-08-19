class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        combs = combinations(arr, 3)
        res = 0
        for comb in combs:
            if self.goodTriple(comb, a, b, c):
                res += 1
        return res

    def goodTriple(self, triplet, a, b, c):
        x = triplet[0]
        y = triplet[1]
        z = triplet[2]
        if -a <= x - y <= a and -b <= y - z <= b and (-c <= x - z <= c):
            return True
        return False
