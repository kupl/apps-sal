class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ans = []
        arr.sort()
        lo, hi = 0, len(arr) - 1
        m = arr[hi // 2]

        while lo <= hi:
            if abs(arr[hi] - m) >= abs(arr[lo] - m):
                ans.append(arr[hi])
                hi -= 1
            else:
                ans.append(arr[lo])
                lo += 1
        return ans[:k]
