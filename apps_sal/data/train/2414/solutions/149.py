class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goods = 0
        for i in range(1, len(arr) - 1):
            first = arr[:i]
            last = arr[i + 1:]
            (ij_count, jk_count, ik_count) = (0, 0, 0)
            (ij_pairs, jk_pairs) = ([], [])
            for n in first:
                if abs(arr[i] - n) <= a:
                    ij_count += 1
                    ij_pairs.append((n, arr[i]))
            for n in last:
                if abs(arr[i] - n) <= b:
                    jk_count += 1
                    jk_pairs.append((arr[i], n))
            print(ij_pairs, jk_pairs)
            for ij in ij_pairs:
                for jk in jk_pairs:
                    if abs(ij[0] - jk[1]) <= c:
                        goods += 1
        return goods
