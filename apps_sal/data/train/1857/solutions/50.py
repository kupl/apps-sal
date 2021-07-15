class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = set(tuple(spot) for spot in reservedSeats)
        reserved_rows = set(spot[0] for spot in reservedSeats)
        res = 0
        for row in reserved_rows:
            first = False
            second = False
            third = False
            
            if all((row, col) not in reserved for col in range(2, 6)):
                first = True
            if all((row, col) not in reserved for col in range(4, 8)):
                second = True
            if all((row, col) not in reserved for col in range(6, 10)):
                third = True

            if first and second and third:
                res += 2
            elif first or second or third:
                res += 1
        
        return res + 2*(n - len(reserved_rows))
