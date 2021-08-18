from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        results = []
        all_indx = list(range(0, len(arr), 1))
        all_triplets = list(combinations(all_indx, 3))
        for idx_tuple in all_triplets:
            arr_i = arr[idx_tuple[0]]
            arr_j = arr[idx_tuple[1]]
            arr_k = arr[idx_tuple[2]]
            if abs(arr_i - arr_j) <= a and abs(arr_j - arr_k) <= b and abs(arr_i - arr_k) <= c:
                results.append(idx_tuple)
        l_results = len(results)
        return l_results
