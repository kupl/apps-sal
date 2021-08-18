class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        median = sorted(arr)[(n - 1) // 2]

        arr_pair = [(x, abs(x - median)) for x in arr]
        arr_pair.sort(key=lambda x: (x[1], x[0]))
        return [x[0] for x in arr_pair[-k:]]
