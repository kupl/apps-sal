class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    one = abs(arr[i] - arr[j])
                    two = abs(arr[j] - arr[k])
                    three = abs(arr[i] - arr[k])
                    if one <= a and two <= b and three <= c:
                        ans += 1
        return ans
