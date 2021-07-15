class Solution:
    def uniquePathsIII(self, grid):

        maxPath = 2
        neighbors = [None] * (len(grid) * len(grid[0]))
        visited = [False] * (len(grid) * len(grid[0]))
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                node = x*len(grid[0]) + y
                if grid[x][y] == 0:
                    neighbors[node] = getNeighbors(grid, x, y)
                    visited[node] = False
                    maxPath += 1
                elif grid[x][y] == 1:
                    start = node
                    neighbors[node] = getNeighbors(grid, x, y)
                elif grid[x][y] == 2:
                    end = node
                    visited[node] = False

        return count(neighbors, visited, start, maxPath, 1, end)

def getNeighbors(grid, x, y):
    output = []
    if x > 0 and grid[x-1][y] % 2 == 0:
        output.append((x-1)*len(grid[0])+y)
    if x < len(grid)-1 and grid[x+1][y] % 2 == 0:
        output.append((x+1)*len(grid[0])+y)
    if y > 0 and grid[x][y-1] % 2 == 0:
        output.append(x*len(grid[0])+y-1)
    if y < len(grid[0]) - 1 and grid[x][y+1] % 2 == 0:
        output.append(x*len(grid[0])+y+1)
    return output
    
def count(neighbors, visited, node, maxPath, pathLength, destination):

    if pathLength == maxPath and node == destination:
        return 1
    elif pathLength == maxPath or node == destination:
        return 0

    visited[node] = True

    sum = 0
    for k in neighbors[node]:
        if not visited[k]:
            sum += count(neighbors, visited, k, maxPath, pathLength + 1, destination)
    
    visited[node] = False
    return sum
