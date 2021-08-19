class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_count = 0
        i = 0
        j = 1
        k = 2
        if len(arr) > 2:
            while i + 2 < len(arr):

                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    good_count += 1
                    # print(\"i:\",i,\" j: \",j,\" k: \",k, \" good_count: \",good_count,\" ijk:\",i,j,k)
                # move k if k != arr.len - 1
                if k != len(arr) - 1:
                    k += 1
                # move j and reset k = j +1 if k == arr.len - 1
                elif k == len(arr) - 1 and j + 1 != k:
                    j += 1
                    k = j + 1
                # move i and reset j = i+1, k = + j+1 if j == arr.len - 2
                elif j == len(arr) - 2:
                    i += 1
                    j = i + 1
                    k = j + 1

        return good_count
