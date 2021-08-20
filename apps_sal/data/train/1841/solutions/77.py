class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        svals = collections.defaultdict(list)
        median = sorted(arr)[(len(arr) - 1) // 2]
        for i in range(len(arr)):
            svals[abs(arr[i] - median)].append(arr[i])
        svals = sorted(svals.items(), key=lambda x: -x[0])
        res = []
        count = 0
        for tuplee in svals:
            flag = True
            for i in sorted(tuplee[1], reverse=True):
                res.append(i)
                count += 1
                if count == k:
                    flag = False
                    break
            if not flag:
                break
        return res
