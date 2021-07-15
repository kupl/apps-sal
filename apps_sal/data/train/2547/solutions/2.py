class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        count = 0
        
        for inside in grid:
            a = 0
            b = len(inside) - 1
            
            while a <= b:
                middle = (a + b)//2
                if inside[middle] < 0:
                    if middle > 0 and inside[middle-1] >= 0:
                        count += (length - middle)
                        break
                    elif middle == 0 and inside[middle-1] < 0:
                        count += length
                        break
                    else:
                        b -= 1
                else:
                    a += 1
                    
        return count

