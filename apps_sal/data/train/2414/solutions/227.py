class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(i+1, length):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, length):
                        if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                            count += 1
        return count
