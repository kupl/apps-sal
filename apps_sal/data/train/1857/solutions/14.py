from collections import defaultdict
class Solution:
#     def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#         reservedSeats.sort()
#         n_res = len(reservedSeats)
#         ans = 2 * n
#         row, res_id = 0, 0
        
#         while res_id < n_res:
#             cur_row = reservedSeats[res_id][0]
            
#             rm = set()
#             while res_id < n_res and reservedSeats[res_id][0] == cur_row:
#                 j = reservedSeats[res_id][1]
#                 if j in (2, 3, 4, 5):
#                     rm.add(0)
#                 if j in (4, 5, 6, 7):
#                     rm.add(1)
#                 if j in (6, 7, 8, 9):
#                     rm.add(2)
#                 res_id += 1
            
#             if len(rm) == 3:
#                 ans -= 2
#             else:
#                 ans -= 1
            
#         return ans
    
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        
        for i,j in reservedSeats:
            if j in [2,3,4,5]:
                seats[i].add(0)
            if j in [4,5,6,7]:
                seats[i].add(1)
            if j in [6,7,8,9]:
                seats[i].add(2)
        
        res = 2*n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1
        return res
