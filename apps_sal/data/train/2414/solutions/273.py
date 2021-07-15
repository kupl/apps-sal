class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplet_count = 0
        for ind_1 in range(0,len(arr)):
            if ind_1 + 2 <=len(arr):             
                for ind_2 in range(ind_1 + 1, len(arr)):
                    if (abs(arr[ind_1] - arr[ind_2]) <= a):
                        for ind_3 in range(ind_2+1,len(arr)):
                                if (abs(arr[ind_1] - arr[ind_2]) <= a) and (abs(arr[ind_2] - arr[ind_3]) <= b) and (abs(arr[ind_1] - arr[ind_3]) <= c):
                                    good_triplet_count = good_triplet_count + 1
        return good_triplet_count
                             
                                        

