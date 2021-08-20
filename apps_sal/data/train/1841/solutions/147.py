class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        orderarr = sorted(arr)
        index = (len(arr) - 1) // 2
        mid = orderarr[index]
        dic = defaultdict(list)
        for i in range(len(orderarr) - 1, -1, -1):
            curabs = abs(orderarr[i] - mid)
            dic[curabs].append(orderarr[i])
        res = []
        keys = sorted(dic.keys())
        for i in range(len(keys) - 1, -1, -1):
            for j in dic[keys[i]]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
