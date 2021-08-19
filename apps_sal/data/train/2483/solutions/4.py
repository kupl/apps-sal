class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = False
        occ = []
        n = 0
        for i in range(0, len(arr)):
            if arr[i] in arr[0:i]:
                pass
            else:
                n = arr.count(arr[i])
                occ.append(n)
        c = 0
        for j in range(0, len(occ)):
            for k in range(j + 1, len(occ)):
                if occ[j] == occ[k]:
                    c = 1
                    res = False
                    break
                else:
                    c = 0
                    res = True
            if c == 1:
                break
        return res
