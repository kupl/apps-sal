# 9:27 -> DNF
# get an island as sets of 1s, bfs, O(|V|), where V is all A[i][j]
# For one of the islands, run bfs from all its nodes to find the other island
# return shortest of such bfs'
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        def get_islands(A):
            island_one = set()
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1 and (i, j) not in island_one:
                        if not island_one:
                            island_one = make_island(A, i, j, set())
                        else:
                            return island_one, make_island(A, i, j, set())
                    
        
        def make_island(A, i, j, visited):
            visited.add((i, j))
            up = A[i][j + 1] if j < len(A[0]) - 1 else 0
            down = A[i][j - 1] if j > 0 else 0
            left = A[i - 1][j] if i > 0 else 0
            right = A[i + 1][j] if i < len(A) - 1 else 0
            if up and (i, j + 1) not in visited:
                make_island(A, i, j + 1, visited)
            if down and (i, j - 1) not in visited:
                make_island(A, i, j - 1, visited)
            if left and (i - 1, j) not in visited:
                make_island(A, i - 1, j, visited)
            if right and (i + 1, j) not in visited:
                make_island(A, i + 1, j, visited)
            return visited
        
        def find_shortest_bridge(A, i, j, start_island, global_dist_map):
            queue = [(i, j)]
            dist_map = { (i, j) : 0 }
            while queue:
                i, j = queue.pop(0)
                neighbors = []
                if (i, j + 1) not in start_island and j < len(A[0]) - 1:
                    neighbors.append((i, j + 1))
                if (i, j - 1) not in start_island and j > 0:
                    neighbors.append((i, j - 1))
                if (i - 1, j) not in start_island and i > 0:
                    neighbors.append((i - 1, j))
                if (i + 1, j) not in start_island and i < len(A) - 1:
                    neighbors.append((i + 1, j))
                for neighbor in neighbors:
                    n_i, n_j = neighbor
                    if A[n_i][n_j] == 1:
                        return dist_map[(i, j)] + 1
                    if neighbor not in global_dist_map or global_dist_map[neighbor] > dist_map[(i, j)] + 1:
                        queue.append(neighbor)
                        global_dist_map[neighbor] = dist_map[neighbor] = dist_map[(i, j)] + 1
            return False
        
        first_island, second_island = get_islands(A)
        
        min_island = first_island if len(first_island) < len(second_island) else second_island
        
        shortest_bridge = len(A)*len(A[0])
        
        global_dist_map = {}
        
        for island in min_island:
            i, j = island
            shortest_bridge_here = find_shortest_bridge(A, i, j, min_island, global_dist_map)
            if shortest_bridge_here:
                shortest_bridge = min(shortest_bridge, shortest_bridge_here)
        
        return shortest_bridge - 1
        
#         first_coords, second_coords = find_shortest_pair(first_island, second_island)
        
#         i, j = first_coords
        
#         return find_shortest_bridge(A, i, j, first_island) - 1

#         shortest_bridge = len(A)*len(A[0])
        
#         for island in first_island:
#             i, j = island
#             shortest_bridge_here = find_shortest_bridge(A, i, j, first_island)
#             if shortest_bridge_here:
#                 shortest_bridge = min(shortest_bridge, shortest_bridge_here)
        
#         return shortest_bridge - 1

