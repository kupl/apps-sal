class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # make a function that will map out one for the islands
        # make a second function that will calculate the paths to the next island
        # make a third function that will traverse the second island and pick the min path
        
        # map out one of the islands
#         self.mapIsland(A)
#         print(A)
#         # explore the 0s
#         for i in range(0, len(A)):
#             for j in range(0, len(A[i])):
#                 if A[i][j] == 'a':
#                     self.calcPath(i, j, A)
#         print(A)
#     def mapIsland(self, a):
#         #find the first 1 and convert that island
#         for i in range(0, len(a)):
#             for j in range(0, len(a[i])):
#                 if a[i][j] == 1:
#                     return self.explore(i, j, a)
                
#     def explore(self, row, col, a):
#         #convert current node to 'a'
#         a[row][col] = 'a'
#         #explore up
#         if row > 0:
#             if a[row-1][col] == 1:
#                 self.explore(row-1, col, a)
#         #explore left
#         if col > 0:
#             if a[row][col-1] == 1:
#                 self.explore(row, col-1, a)
#         #explore right
#         if col < len(a[row])-1:
#             if a[row][col+1] == 1:
#                 self.explore(row, col +1, a)
#         #explore down
#         if row < len(a)-1:
#             if a[row+1][col] == 1:
#                 self.explore(row +1, col, a)
    
#     def calcPath(self, row, col, a):
#         #take the current a and check if there are any 0s to inverement
#         # if we are at a non 0 look at the neighbors and if they are 0, increment otherwise leave as is?
#         new = 0
#         if a[row][col] == 'a':
#             new = 2
#         else:
#             new = a[row][col]+1
#         #explore up
#         if row > 0:
#             if a[row-1][col] != 1 and a[row-1][col] != 'a' and (a[row][col] == 'a' or a[row][col] > a[row-1][col]):
#                 print(a[row-1][col])
#                 print(new)
#                 a[row-1][col] = min(new, a[row-1][col]) if a[row-1][col] != 0 else new
#                 print(a[row-1][col])
#                 print(a)
#                 self.calcPath(row-1, col, a)
#         #explore left
#         if col > 0:
#             if a[row][col-1] != 1 and a[row][col-1] != 'a' and (a[row][col] == 'a' or a[row][col] > a[row][col-1]):
#                 print(a[row][col-1])
#                 print(new)
#                 a[row][col-1] = min(new, a[row][col-1]) if a[row][col-1] != 0 else new
#                 print(a[row][col-1])
#                 print(a)
                
#                 self.calcPath(row, col-1, a)
#         #explore right
#         if col < len(a[row])-1:
#             if a[row][col+1] != 1 and a[row][col+1] != 'a' and (a[row][col] == 'a' or a[row][col] > a[row][col+1]):
#                 print(a[row][col+1])
#                 print(new)
#                 a[row][col+1] = min(new, a[row][col+1]) if a[row][col+1] != 0 else new
#                 print(a[row][col+1])
#                 print(a)
#                 self.calcPath(row, col +1, a)
#         #explore down
#         if row < len(a)-1:
#             if a[row+1][col] != 1 and a[row+1][col] != 'a' and (a[row][col] == 'a' or a[row][col] > a[row+1][col]):
#                 print(a[row+1][col])
#                 print(new)
#                 a[row+1][col] = min(new, a[row+1][col]) if a[row+1][col] != 0 else new
#                 print(a[row+1][col])
#                 print(a)
#                 self.calcPath(row +1, col, a)
                

        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        # print source, target
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)

