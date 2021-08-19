from collections import defaultdict


class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ij = defaultdict(set)
        jk = defaultdict(set)
        ik = defaultdict(set)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    ij[i].add(j)
                if abs(arr[i] - arr[j]) <= b:
                    jk[i].add(j)
                if abs(arr[i] - arr[j]) <= c:
                    ik[i].add(j)
        ans = 0
        for i in ij:
            for j in ij[i]:
                for k in jk[j]:
                    if k in ik[i]:
                        ans += 1
        return ans
