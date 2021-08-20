class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        con = combinations(arr, 3)
        res = []
        for i in con:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and (abs(i[0] - i[2]) <= c):
                res.append(i)
        return len(res)
