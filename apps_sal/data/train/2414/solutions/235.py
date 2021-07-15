class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total_triplets = 0
        
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c):
                            total_triplets += 1
        return total_triplets

