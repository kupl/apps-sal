class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.map = A
        self.rows = len(self.map)
        self.cols = len(self.map[0])
        
        self.queue = []
        
        # Source island index: 2
        self.src = 2
        # Destination island index: 3
        self.dst = 3
        for island_index in [self.src, self.dst]:
            add_to_queue = (island_index == self.src)
            self.exploreIsland(island_index, add_to_queue)
            
        return self.bridgeBFS()
        
    def exploreIsland(self, index, add):
        row, col = self.getIslandLocation()
        self.islandDFS(index, row, col, add)
    
    def getIslandLocation(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.map[row][col] == 1: return (row, col)
    
    def islandDFS(self, index, row, col, add):
        if self.validCoords(row, col) and self.map[row][col] == 1:
            self.map[row][col] = index
            if add: self.queue.append((row, col, 0))
            for search_row in range(row - 1, row + 2, 2):
                self.islandDFS(index, search_row, col, add)
            for search_col in range(col - 1, col + 2, 2):
                self.islandDFS(index, row, search_col, add)
                
    def validCoords(self, row, col):
        if row < 0 or row >= self.rows:
            return False
        if col < 0 or col >= self.cols:
            return False
        return True
    
    def bridgeBFS(self):
        while len(self.queue) > 0:
            row, col, dist = self.queue.pop(0)
            for search_row in range(row - 1, row + 2, 2):
                if self.processCoord(search_row, col, dist): return dist
            for search_col in range(col - 1, col + 2, 2):
                if self.processCoord(row, search_col, dist): return dist
    
    def processCoord(self, row, col, dist):
        if not self.validCoords(row, col): return False
        if self.map[row][col] == self.dst:
            return True
        elif self.map[row][col] != self.src:
            self.queue.append((row, col, dist + 1))
            self.map[row][col] = self.src
        return False

