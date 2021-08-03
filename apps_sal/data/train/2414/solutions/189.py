class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        initial_last_step_of_i = length - 2
        initial_first_step_of_i = 0
        initial_last_step_of_j = length - 1
        initial_first_step_of_j = 1
        initial_last_step_of_k = length
        initial_first_step_of_k = 2

        triplets = 0

        first_step_of_j = initial_first_step_of_j

        for i in range(initial_first_step_of_i, initial_last_step_of_i):
            first_step_of_k = initial_first_step_of_k
            for j in range(first_step_of_j, initial_last_step_of_j):
                for k in range(first_step_of_k, initial_last_step_of_k):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c and i < j < k:
                        triplets += 1
                first_step_of_k += 1
            first_step_of_j += 1

        return triplets
