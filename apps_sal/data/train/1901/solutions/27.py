class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        label = 1
       
        sum_of_area = 0
        max_area = 0
        map_info = {}
        grid_info = copy.deepcopy(grid)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    area = self.findIsland(grid, grid_info, i, j, R, C, label)
                    map_info[label] = area
                    sum_of_area += area
                    label += 1
                
        print(map_info)
        print(grid_info)
        
        
        for i in range(R):
            for j in range(C):
                if grid_info[i][j] == 0:
                    current = self.testChange(grid_info, i, j, R, C, map_info)
                    if current > max_area:
                        max_area = current
        
        if max_area == 0:
            max_area = sum_of_area
                
        return max_area
        
        
    def testChange(self, grid_info, i, j, R, C, map_info):
        
        island = []
        area = 0
        if 0 <= i+1 < R and grid_info[i+1][j] > 0:
            island.append(grid_info[i+1][j])
        
        if 0 <= i-1 < R and grid_info[i-1][j] > 0:
            island.append(grid_info[i-1][j])
        
        if 0 <= j+1 < C and grid_info[i][j+1] > 0:
            island.append(grid_info[i][j+1])
        
        if 0 <= j-1 < C and grid_info[i][j-1] > 0:
            island.append(grid_info[i][j-1])
            
        if not island: 
            return 1
        
        for key in list(map_info.keys()):
            if key in island:
                area += map_info[key]
                
        return area + 1
        
    def findIsland(self, grid, grid_info, i, j, R, C, label):
        
        area = 0
        
        if  (i >= R or j >= C or i < 0 or j < 0) or grid[i][j] == 0:
            return 0
        else:
            area = grid[i][j]
            grid_info[i][j] = label
            grid[i][j] = 0
            
        return area + self.findIsland(grid, grid_info, i, j+1, R, C, label) + self.findIsland(grid, grid_info, i, j-1, R, C, label) + self.findIsland(grid, grid_info, i+1, j, R, C, label) + self.findIsland(grid, grid_info, i-1, j, R, C, label)
        
            

