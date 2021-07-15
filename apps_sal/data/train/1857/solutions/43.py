class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat_dict = {}
        
        for seat in reservedSeats:

            row, col = seat
            temp = seat_dict.get(row, set())
            temp.add(col)
            seat_dict[row] = temp

                
        res = 0
        for row in seat_dict.keys():
            row_situ = seat_dict[row]
            if 4 not in row_situ and \\
               5 not in row_situ and \\
               6 not in row_situ and \\
               7 not in row_situ:
                res += 1
            
                if ((2 not in row_situ) and \\
                   (3 not in row_situ) and \\
                   (8 not in row_situ) and \\
                   (9 not in row_situ)):
                    res += 1
            else:
                if ((2 not in row_situ) and \\
                   (3 not in row_situ) and \\
                   (4 not in row_situ) and \\
                   (5 not in row_situ)):
                    res += 1
                
                if ((6 not in row_situ) and \\
                   (7 not in row_situ) and \\
                   (8 not in row_situ) and \\
                   (9 not in row_situ)):
                    res += 1
        res += 2*(n-len(seat_dict.keys()))
        return res
        
        
