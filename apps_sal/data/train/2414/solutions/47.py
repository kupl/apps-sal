class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        di = defaultdict(set)
        dj = defaultdict(set)
        dk = defaultdict(set)
        arr = [(i, x) for (i, x) in enumerate(arr)]
        arr = sorted(arr, key=lambda x: x[1])
        n = len(arr)
        for (i, tup_a) in enumerate(arr):
            (iorig, x) = tup_a
            j = i + 1
            while True:
                if j == n:
                    break
                if abs(x - arr[j][1]) <= a:
                    di[iorig].add(arr[j][0])
                if abs(x - arr[j][1]) <= b:
                    dj[iorig].add(arr[j][0])
                if abs(x - arr[j][1]) <= c:
                    dk[iorig].add(arr[j][0])
                j += 1
            j = i - 1
            while True:
                if j < 0:
                    break
                if abs(x - arr[j][1]) <= a:
                    di[iorig].add(arr[j][0])
                if abs(x - arr[j][1]) <= b:
                    dj[iorig].add(arr[j][0])
                if abs(x - arr[j][1]) <= c:
                    dk[iorig].add(arr[j][0])
                j -= 1
        o = 0
        for i in range(n):
            for j in di[i]:
                for k in dj[j]:
                    if k in dk[i]:
                        if i >= 0 and j > i and (k > j) and (k < n):
                            o += 1
        return o
