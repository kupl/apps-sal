'''
Ad-Hoc:
Only following configs are possible:
config1 = {2,3,4,5,6,7,8,9} -> 2 groups
config2 = {2,3,4,5} -> 1 group
config3 = {4,5,6,7} -> 1 group
config4 = {6,7,8,9} -> 1 group
'''
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        rowSeats = defaultdict(set)
        occupiedRows = set()
        freeRows = n
        
        for seatRow, seatNum in reservedSeats:
            rowSeats[seatRow].add(seatNum)
            if seatRow not in occupiedRows:
                occupiedRows.add(seatRow)
                freeRows -= 1
            
        config1 = {2,3,4,5,6,7,8,9}
        config2 = {2,3,4,5}
        config3 = {4,5,6,7}
        config4 = {6,7,8,9}
        
        #print(rowSeats, config1.intersection(rowSeats[1]))
        res = freeRows*2
        for row in rowSeats:
            if len(rowSeats[row]) == 0 or not config1.intersection(rowSeats[row]):
                res += 2
            else:
                res += int(not config2.intersection(rowSeats[row]) or not config3.intersection(rowSeats[row]) or not config4.intersection(rowSeats[row]))
        
        return res
