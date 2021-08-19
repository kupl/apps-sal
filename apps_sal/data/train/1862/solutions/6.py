class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # Discussion solution by Lee215
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res

        # First answer: Best run 93.4%[36ms], 5.03%[14.2MB]
        out = []
        for i in range(len(arr), 0, -1):  # traverse left-to-right
            if arr[i - 1] != i:           # find 1st wrong entry
                j = arr.index(i)        # search for right entry
                out.extend([j + 1, i])
                arr[:j + 1] = reversed(arr[:j + 1])
                arr[:i] = reversed(arr[:i])
        return out
