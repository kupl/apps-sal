class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        it_arr = []
        i = 1
        while len(it_arr) < k + 1:
            if i not in arr:
                it_arr.append(i)
            i += 1
        return it_arr[k - 1]
