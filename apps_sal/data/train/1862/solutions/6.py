class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res

        out = []
        for i in range(len(arr), 0, -1):
            if arr[i - 1] != i:
                j = arr.index(i)
                out.extend([j + 1, i])
                arr[:j + 1] = reversed(arr[:j + 1])
                arr[:i] = reversed(arr[:i])
        return out
