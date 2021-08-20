from collections import defaultdict as d


class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        (da, db, dc) = (d(set), d(set), d(set))
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                k = abs(arr[i] - arr[j])
                if k <= a:
                    da[i].add(j)
                if k <= b:
                    db[i].add(j)
                if k <= c:
                    dc[i].add(j)
        res = 0
        for i in da:
            for j in da[i]:
                res += len(db[j] & dc[i])
        return res
