class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        median = sorted(arr)[(n - 1) // 2]

        arr_pair = [(i, abs(arr[i] - median)) for i in range(n)]
        arr_pair.sort(key=lambda x: (x[1], arr[x[0]]))
        return [arr[x[0]] for x in arr_pair[-k:]]
