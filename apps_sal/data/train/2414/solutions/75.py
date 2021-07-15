from itertools import combinations

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
    
        # Brute Force
        # Time: O(n^3)   
    
#         size = len(arr)
#         for i in range(size):
#             for j in range(size):
#                 if i >= j:
#                     continue
#                 for k in range(size):
#                     if i >= k or j >= k:
#                         continue
                    
#                     if (abs(arr[i] - arr [j]) <= a) and (abs(arr[j] - arr [k]) <= b) and (abs(arr[i] - arr [k]) <= c) :
#                         count += 1



        # Using itertools.combinations
    
        # triplets = combinations(arr, 3)
        # for triplet in triplets:
        #     if (abs(triplet[0] - triplet[1]) <= a) \\
        #             and (abs(triplet[1] - triplet[2]) <= b) \\
        #             and (abs(triplet[0] - triplet[2]) <= c):
        #         count += 1
        # return count

        
        combs = combinations(arr, 3)
        return sum((abs(comb[0] - comb[1]) <= a and abs(comb[1] - comb[2]) <= b and abs(comb[0] - comb[2]) <= c) for comb in combs)
