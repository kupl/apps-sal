class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ma = {}
        (d, psum) = (set(), [])

        def add(p):
            for i in range(ma[p], len(psum)):
                psum[i] += 1

        def get(l, r):
            if l > r:
                return 0
            return psum[ma[r]] - psum[ma[l] - 1]
        n = len(arr)
        d.add(-sys.maxsize)
        for i in arr:
            d.add(i)
            d.add(i + a)
            d.add(i - a)
            d.add(i + c)
            d.add(i - c)
        d = sorted(list(d))
        for (i, v) in enumerate(d):
            ma[v] = i
        psum = [0] * len(d)
        ans = 0
        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) > b:
                    continue
                l = max(arr[j] - a, arr[k] - c)
                r = min(arr[j] + a, arr[k] + c)
                ans += get(l, r)
            add(arr[j])
        return ans
