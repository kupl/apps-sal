class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        iterator = list(range(len(arr)))
        count = 0
        for i in iterator:
            for j in iterator:
                if i < j < len(arr):
                    if abs(arr[i] - arr[j]) <= a:
                        for k in iterator:
                            if i < j < k < len(arr):
                                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                                    count += 1
        return count
