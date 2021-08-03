from collections import defaultdict


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        da = defaultdict(set)
        db = defaultdict(set)
        dc = defaultdict(set)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if(abs(arr[i] - arr[j]) <= a):
                    da[i].add(j)
                if(abs(arr[i] - arr[j]) <= b):
                    db[i].add(j)
                if(abs(arr[i] - arr[j]) <= c):
                    dc[i].add(j)
        for i in da:
            for j in da[i]:
                for k in db[j]:
                    if k in dc[i]:
                        count += 1
        return count
