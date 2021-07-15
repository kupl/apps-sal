class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        options = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        flip_req = float('inf')
        isl_one_coords = set()
        
        
        def get_all(i, j):
            nonlocal flip_req, isl_one_coords, options
            for opt in options:
                new_coord = (i + opt[0], j + opt[1])
                if 0 <= new_coord[0] < len(A) and 0 <= new_coord[1] < len(A[0]):
                    if A[new_coord[0]][new_coord[1]] and not new_coord in isl_one_coords:
                        isl_one_coords.add(new_coord)
                        get_all(new_coord[0], new_coord[1])
            
        
        def bfs():
            nonlocal flip_req, isl_one_coords, options
            dist = 0
            level = set([x for x in isl_one_coords])
            next_level = set()
            while level:
                for coords in level:
                    for opt in options:
                        new_coord = (coords[0] + opt[0], coords[1] + opt[1])
                        if 0 <= new_coord[0] < len(A) and 0 <= new_coord[1] < len(A[0]) and not new_coord in isl_one_coords:
                            if A[new_coord[0]][new_coord[1]]:
                                return dist
                            if not A[new_coord[0]][new_coord[1]]:
                                isl_one_coords.add(new_coord)
                                next_level.add(new_coord)
                dist += 1
                level, next_level = next_level, set()
                print((level, next_level, isl_one_coords))
                

            
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]: 
                    isl_one_coords.add((i, j))
                    get_all(i, j)
                    return bfs()

