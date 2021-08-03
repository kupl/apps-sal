class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i < j:
                        if j < k:
                            if abs(arr[i] - arr[j]) <= a:
                                if abs(arr[j] - arr[k]) <= b:
                                    if abs(arr[i] - arr[k]) <= c:
                                        good_count += 1
        return good_count
