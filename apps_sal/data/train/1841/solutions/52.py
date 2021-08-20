class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        import functools

        def comparator(n1, n2):
            if abs(n1 - m) > abs(n2 - m):
                return 1
            if abs(n1 - m) < abs(n2 - m):
                return -1
            if abs(n1 - m) == abs(n2 - m):
                if n1 > n2:
                    return 1
                elif n1 < n2:
                    return -1
                else:
                    return 0
            return 0
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        new = sorted(arr, key=functools.cmp_to_key(comparator), reverse=True)
        return new[:k]
