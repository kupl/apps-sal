class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        mid = arr[(n - 1) // 2]
        h = collections.defaultdict(list)
        for i in arr:
            h[abs(i - mid)].append(i)
        sorted_data = sorted(h.items(), reverse=True)
        res = []
        for j in sorted_data:
            while len(j[1]) != 0:
                res.append(j[1].pop(-1))
                k -= 1
                if k == 0:
                    return res
        return res
