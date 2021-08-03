class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i = 0
        j = i + 1
        k = j + 1
        return_arr = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range(j, len(arr)):
                    if i < j < k:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            return_arr.append([arr[i], arr[j], arr[k]])

        return len(return_arr)
