class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 1:
            return arr
        arr.sort()
        med_loc = (len(arr) - 1) // 2
        median = arr[med_loc]
        count = 0
        ans = []
        while count < k:
            if abs(arr[0] - median) > abs(arr[-1] - median):
                ans.append(arr[0])
                arr.pop(0)
            else:
                ans.append(arr[-1])
                arr.pop()
            count += 1

        return ans
