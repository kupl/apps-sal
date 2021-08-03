class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        if k >= len(arr):
            return arr

        median = self.get_median(arr)

        results = [(math.fabs(arr[x] - median), arr[x]) for x in range(len(arr))]
        results.sort()

        return [results[-i - 1][1] for i in range(k)]

    def get_median(self, arr):

        arr_sorted = sorted(arr)
        idx = int((len(arr) - 1) / 2)
        return arr_sorted[idx]
