class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        good = 0
        for i in range(0, n):
            ai = arr[i]
            for j in range(i + 1, n):
                aj = arr[j]
                if abs(ai - aj) > a:
                    continue
                for k in range(j + 1, n):
                    ak = arr[k]
                    if abs(aj - ak) > b:
                        continue
                    if abs(ak - ai) > c:
                        continue
                    good += 1
        return good
