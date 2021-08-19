class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        print(arr)
        print((a, b, c))
        resp = []
        count = 0
        comb = itertools.combinations(arr, 3)
        for i in comb:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and (abs(i[0] - i[2]) <= c):
                resp.append(i)
                count = count + 1
        return count
