class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # we perform bfs to find connected components and from all the connected components we remove those that have a node on the edges
        # first we create a set of nodes that can act as start nodes
        possible_start = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    possible_start.add((i, j))
        # now we need to perform bfs from each possible start and find the connected components
        answer = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while possible_start != set():
            start = possible_start.pop()
            # print('start',start)
            queue = [start]
            visited = set([start])
            if 0 == start[0] or start[0] == len(grid) - 1 or 0 == start[1] or start[1] == len(grid[1]) - 1:
                remove_this_island = True
            else:
                remove_this_island = False
            while queue != []:
                c = queue.pop(0)
                # print(c)
                for d in directions:
                    n = (c[0] + d[0], c[1] + d[1])
                    if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]):
                        if grid[n[0]][n[1]] == 0:
                            if 0 == n[0] or n[0] == len(grid) - 1 or 0 == n[1] or n[1] == len(grid[1]) - 1:
                                remove_this_island = True
                            if n not in visited:
                                queue.append(n)
                                visited.add(n)

            # print(visited,remove_this_island)
            # at the end of the bfs we check if we need to consider this island or not
            possible_start = possible_start - visited
            if not remove_this_island:
                answer += 1

        return answer
