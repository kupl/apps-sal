class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        L = len(arr)
        output = 0
        for i in range(L - 2):
            for j in range(i + 1, L - 1):
                for k in range(j + 1, L):
                    if (abs(arr[i] - arr[j]) <= a) + (abs(arr[j] - arr[k]) <= b) + (abs(arr[i] - arr[k]) <= c) == 3:
                        output += 1
        return output
