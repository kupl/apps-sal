class Solution:

    def countLargestGroup(self, n: int) -> int:
        arr = [0] * 36
        for i in range(1, n + 1):
            sm = 0
            for j in str(i):
                sm += int(j)
            arr[sm - 1] += 1
        count = 0
        mx = max(arr)
        for i in arr:
            if i == mx:
                count += 1
        return count
