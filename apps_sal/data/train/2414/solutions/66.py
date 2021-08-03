from collections import defaultdict


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        lt_a = defaultdict(set)
        lt_b = defaultdict(set)
        lt_c = defaultdict(set)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[j] - arr[i]) <= a:
                    lt_a[i].add(j)
                if abs(arr[j] - arr[i]) <= b:
                    lt_b[i].add(j)
                if abs(arr[j] - arr[i]) <= c:
                    lt_c[i].add(j)

        num_good_triplets = 0
        for i in lt_a:
            for j in lt_a[i]:
                for k in lt_b[j]:
                    if k in lt_c[i]:
                        num_good_triplets += 1

        return num_good_triplets
