class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        combs = combinations(arr, 3)
        count = 0
        for i in combs:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and (abs(i[0] - i[2]) <= c):
                count += 1
        return count
