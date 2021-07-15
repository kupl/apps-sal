class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_reservations = dict()
        for reserve in reservedSeats:
            row, col = reserve
            if row not in row_reservations:
                row_reservations[row] = set()
            row_reservations[row].add(col)
        
        total = 0
        left = set([2,3,4,5])
        right = set([6,7,8,9])
        center = set([4,5,6,7])
        for row in row_reservations:
            r = row_reservations[row]
            
            if (left & r and right & r and center & r):
                n -= 1
                continue
            
            if not left & r and not right & r:
                total += 2
            else:
                total += 1
            n -= 1
        
        return total + (n * 2)
