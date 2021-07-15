class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seatmap = collections.defaultdict(list)
        
        for row in reservedSeats:
            seatmap[row[0]].append(row[1])
        
        ans = 0
        for row in list(seatmap.keys()):
            
            if len(seatmap[row]) == 1:
                if seatmap[row][0] == 1 or seatmap[row][0] == 10:
                    ans += 2
                else:
                    ans += 1
            else:
                row_arrange = [0] * 10
                for each in seatmap[row]:
                    row_arrange[each-1] = 1

                if row_arrange[1:5] == [0, 0, 0, 0]:
                    ans += 1
                if row_arrange[5:9] == [0, 0, 0, 0]:
                    ans += 1
                if row_arrange[3:7] == [0, 0, 0, 0] and row_arrange[1:3] != [0, 0] and row_arrange[7:9] != [0, 0]:
                    ans += 1
        
        return ans + (n - len(seatmap))*2

