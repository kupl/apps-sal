class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        good_triplets = 0
        arr_len = len(arr)
        for i in range(arr_len):
            # print(\"i: \" + str(i))
            for j in range(i + 1, arr_len):
                # print(\"\\tj: \" + str(j))
                for k in range(j + 1, arr_len):
                    # print(\"\\t\\tk: \" + str(k))
                    if((0 <= i and i < j and j < k and k < len(arr)) and (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c)):
                        triplet = [i, j, k]
                        # print(triplet)
                        good_triplets += 1
        return good_triplets
