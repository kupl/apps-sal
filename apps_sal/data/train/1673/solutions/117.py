class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        MAX_V = int(1000000000.0)
        min_v = [0] * n
        for i in range(n):
            row = arr[i]
            new_min_v = [MAX_V] * n
            scan_min = min_v[-1]
            for i in range(n - 2, -1, -1):
                new_min_v[i] = min(new_min_v[i], scan_min + row[i])
                scan_min = min(scan_min, min_v[i])
            scan_min = min_v[0]
            for i in range(1, n):
                new_min_v[i] = min(new_min_v[i], scan_min + row[i])
                scan_min = min(scan_min, min_v[i])
            min_v = new_min_v
        return min(min_v)
