class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        if len(arr) == 0:
            return []

        if k == len(arr):
            return sorted(arr)

        arr.sort()

        l = len(arr)

        med = arr[(l - 1) // 2]

        arr = [(abs(n - med), n) for n in arr]

        from functools import cmp_to_key

        def cmp(x, y):

            if x[0] == y[0]:
                if x[1] > y[1]:
                    return -1
                elif x[1] < y[1]:
                    return 1
                else:
                    return 0
            elif x[0] > y[0]:
                return -1
            else:
                return 1

        res = sorted(arr, key=cmp_to_key(cmp))

        return [res[i][1] for i in range(k)]
