class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        arr_pair = [(i, arr[i]) for i in range(n)]
        arr_pair.sort(key=lambda x: x[1])
        median = arr_pair[(n - 1) // 2][1]
        max_val = max([abs(x) for x in arr])

        arr_pair = [(x[0], abs(x[1] - median)) for x in arr_pair]
        arr_pair.sort(key=lambda x: (x[1], arr[x[0]]))

        return [arr[x[0]] for x in arr_pair[-k:]]
