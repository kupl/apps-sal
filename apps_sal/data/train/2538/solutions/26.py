class Solution:

    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        arr = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        for i in range(10, n + 1):
            k = list(map(int, list(str(i))))
            k = sum(k)
            print(k)
            if k <= len(arr):
                arr[k - 1].append(i)
            else:
                arr.append([k])
        arr = sorted(arr, key=len, reverse=True)
        print(arr)
        l = len(arr[0])
        i = 0
        while i < len(arr) and len(arr[i]) == l:
            i += 1
        return i
