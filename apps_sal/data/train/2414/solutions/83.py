from collections import defaultdict


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        da = defaultdict(set)
        db = defaultdict(set)
        dc = defaultdict(set)
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                dis = abs(arr[j] - arr[i])
                if dis <= a:
                    da[i].add(j)
                if dis <= b:
                    db[i].add(j)
                if dis <= c:
                    dc[i].add(j)
        count = 0
        for i in range(len(arr) - 2):
            for j in da[i]:
                for k in db[j]:
                    if k in dc[i]:
                        count += 1
        return count
