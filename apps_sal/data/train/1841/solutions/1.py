class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        ans = []
        lt = 0
        pt = len(arr) - 1
        m = arr[(len(arr) - 1) // 2]
        for i in range(k):
            left = abs(arr[lt] - m)
            right = abs(arr[pt] - m)
            if right >= left:
                ans.append(arr[pt])
                pt -= 1
            else:
                ans.append(arr[lt])
                lt += 1
        return ans
