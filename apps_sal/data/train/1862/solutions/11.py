class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            for i in range(k // 2):
                arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]

        ans = []
        val = len(arr)
        while val > 0:
            i = arr.index(val)
            if 0 < i < val - 1:
                ans.append(i + 1)
                flip(i + 1)
            if i < val - 1:
                ans.append(val)
                flip(val)
            val -= 1
        return ans
