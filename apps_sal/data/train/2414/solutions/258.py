class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        arr_len = len(arr)
        for i in range(arr_len - 2):
            for j in range(i + 1, arr_len - 1):
                if j < i:
                    break
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, arr_len):
                        if k < j:
                            break
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            triplet = [i, j, k]
                            good_triplets += 1
        return good_triplets
