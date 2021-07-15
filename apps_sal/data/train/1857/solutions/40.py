class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Beware of aisle split
        # Only have a few configurations to sit 4 people in a given row
        # 1) [4, 5, 6, 7]
        # 2) [2, 3, 4, 5]
        # 3) [6, 7, 8, 9]
        # 4) (2) AND (3)
        
        
        # Brute force: Walk over all the rows O(n^2), with a map of seatOccupied[row][seat_number] = True
        # Better: Sort reserved seats by row, then seat_number: 2*O(logn)
        # Best: O(n) make a map, O(n) walk over rows
        
        
        occupied = collections.defaultdict(set)
        for reservedSeat in reservedSeats:
            row = reservedSeat[0]
            seat_number = reservedSeat[1]
            
            if seat_number in [4, 5]:
                # Center, Left are occupied
                occupied[row].add(\"C\")
                occupied[row].add(\"L\")
            elif seat_number in [6, 7]:
                # Center, Right are occupied
                occupied[row].add(\"C\")
                occupied[row].add(\"R\")
            elif seat_number in [2, 3]:
                # Left is occupied
                occupied[row].add(\"L\")
            elif seat_number in [8, 9]:
                # Right is occupied
                occupied[row].add(\"R\")
        
        empty_rows: int = n
        total: int = 0
        for row in occupied:
            empty_rows -= 1
            left = \"L\" not in occupied[row]
            right = \"R\" not in occupied[row]
            center = \"C\" not in occupied[row]

            if left and right:
                total += 2
            elif left or right or center:
                total += 1
        
        
        return total + 2 * empty_rows
                
            
            
        
        
