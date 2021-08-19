class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        d = {}
        sort = sorted(arr)
        if n % 2 == 1:
            m = sort[n // 2]
        else:
            m = sort[(n - 1) // 2]
        for num in arr:
            val = abs(num - m)
            if val not in d:
                d[val] = []
            d[val].append(num)
        items = sorted(list(d.items()), reverse=True)
        i = 0
        ret = []
        while i < len(items) and k > 0:
            if k >= len(items[i][1]):
                ret.extend(items[i][1])
                k -= len(items[i][1])
            else:
                break
            i += 1
        if k > 0:
            items[i][1].sort()
            for j in range(k):
                ret.append(items[i][1][len(items[i][1]) - j - 1])
        return ret
