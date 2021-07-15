class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i, n_i in enumerate(arr[:-2]):
            for j in range(i+1, len(arr)-1):
                n_j = arr[j]
                for n_k in arr[j+1:]:
                    if abs(n_i - n_j) <= a and abs(n_j - n_k) <= b and abs(n_i - n_k) <=c:
                        count += 1
        return count
