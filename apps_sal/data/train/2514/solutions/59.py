from collections import Counter


class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        cnt = Counter(arr2)
        for n in arr1:
            td = d
            vals_to_find = []
            while td >= -d:
                vals_to_find.append(n - td)
                td -= 1
            add = True
            for j in vals_to_find:
                if cnt[j] > 0:
                    add = False
                    break
            if add:
                res += 1
        return res
