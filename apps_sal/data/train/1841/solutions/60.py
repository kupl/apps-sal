class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        cnt = len(arr)
        arr = sorted(arr)
        mid_id = (cnt - 1) // 2
        mid = arr[mid_id]
        if k == cnt:
            return arr

        curr = 0
        res = []
        left, right = 0, cnt - 1
        while curr < k:
            if abs(arr[right] - mid) >= abs(mid - arr[left]):
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
            curr += 1

        return res
