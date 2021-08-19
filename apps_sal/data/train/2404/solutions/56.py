class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        start = 1
        i = 0
        while i < len(arr):
            print(start, arr[i])
            if k == 0:
                return start - 1
            if start != arr[i]:
                k -= 1
                start += 1
            elif start == arr[i]:
                start += 1
                i += 1
        if k > 0:
            return start + k - 1
