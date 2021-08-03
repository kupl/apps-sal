class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cou = 0
        left, right = 0, len(arr) - 1
        while left < len(arr) - 2:
            if left == right - 1:
                left += 1
                right = len(arr) - 1
                continue
            if abs(arr[left] - arr[right]) > c:
                right -= 1
                continue
            cou += sum([abs(arr[left] - arr[i]) <= a and abs(arr[i] - arr[right]) <= b for i in range(left + 1, right)])
            right -= 1
        return cou

        return sum([
            abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c
            for i in range(len(arr))
            for j in range(i + 1, len(arr))
            for k in range(j + 1, len(arr))
        ])
