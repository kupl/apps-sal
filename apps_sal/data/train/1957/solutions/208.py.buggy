import heapq
from collections import deque
from typing import List, Dict, Tuple

class Solution:

    def getNeighbors(self, grid: List[List[int]], ycor: int, xcor: int) -> List[List[int]]:

        directions = [
            (-1, 0),
            (1,  0),
            (0,  1),
            (0, -1)
        ]

        neighbors = []

        for delta_y, delta_x in directions:

            new_y = ycor + delta_y
            new_x = xcor + delta_x

            if new_y > -1 and new_y < len(grid) and \\
               new_x > -1 and new_x < len(grid[0]):

                neighbors.append( (new_y, new_x) )

        return neighbors


    def v0(self, grid: List[List[int]], k: int) -> int:

        # Start at 0,0, with 0 distance traveled, and 0 blocks destroyed.
        queue = deque([ (0, 0, 0, 0) ])

        # Keep a visited set so we don't end up in a cycle.
        visited = set([])

        while queue:

            ycor, xcor, num_steps, destroyed = queue.popleft()

            if ycor == len(grid) - 1 and xcor == len(grid[0]) - 1:
                return num_steps

            # Adding to visited after we enter it, makes this solution more
            # symmetric to the Djikstra type questions.
            elif (ycor, xcor) not in visited:

                visited.add( (ycor, xcor) )

                for neighbor_y, neighbor_x in self.getNeighbors(grid, ycor, xcor):

                    if grid[neighbor_y][neighbor_x] in (0, '0'):
                        queue.append( (neighbor_y, neighbor_x, num_steps + 1, destroyed) )
                    elif destroyed < k:
                        queue.append( (neighbor_y, neighbor_x, num_steps + 1, destroyed + 1) )

        return -1


    def v1(self, grid: List[List[int]], k: int) -> int:
        \"\"\"
        Welp, somewhere deep in the test cases, my original solution breaks,
        presumably due to my \"visited\" strategy closing off a path that
        includes destroying a block even though it's shorter.
        \"\"\"
        # Start at 0,0, with 0 distance traveled, and 0 blocks destroyed.
        queue = [ (0, 0, 0, 0) ]

        # Keep a visited set so we don't end up in a cycle.
        visited = set([])

        while queue:

            num_steps, ycor, xcor, destroyed = heapq.heappop(queue)

            if ycor == len(grid) - 1 and xcor == len(grid[0]) - 1:
                return num_steps

            # Adding to visited after we enter it, makes this solution more
            # symmetric to the Djikstra type questions.
            elif (ycor, xcor, destroyed) not in visited:

                visited.add( (ycor, xcor, destroyed) )

                for neighbor_y, neighbor_x in self.getNeighbors(grid, ycor, xcor):

                    if grid[neighbor_y][neighbor_x] in (0, '0'):
                        heapq.heappush( queue, ( num_steps + 1, neighbor_y, neighbor_x, destroyed) )
                    elif destroyed < k:
                        heapq.heappush( queue, ( num_steps + 1, neighbor_y, neighbor_x, destroyed + 1) )

        return -1


    def dfs(self, grid: List[List[int]], ycor: int, xcor: int,
            destroys_remaining: int, steps_taken: int, path: List[int]) -> int:
        \"\"\"
        The sub-worker function.
        \"\"\"
        if ycor == len(grid) - 1 and xcor == len(grid[0]) - 1:
            return steps_taken

        else:

            sub_paths = []

            min_sub_path = float('inf')
            min_y = None
            min_x = None

            for neighbor_y, neighbor_x in self.getNeighbors(grid, ycor, xcor):

                # We'll keep a local history of points visited in the current
                # path, rather than a nonlocal \"visited\" set.
                if (neighbor_y, neighbor_x) not in path:

                    possible = float('inf')

                    if grid[neighbor_y][neighbor_x] in (0, '0'):
                        possible = self.dfs(grid, neighbor_y, neighbor_x,
                                            destroys_remaining, steps_taken + 1,
                                            path + [(neighbor_y, neighbor_x)])

                    elif destroys_remaining > 0:
                        possible = self.dfs(grid, neighbor_y, neighbor_x,
                                            destroys_remaining - 1, steps_taken + 1,
                                            path + [(neighbor_y, neighbor_x)])

                    if possible < min_sub_path:
                        min_sub_path = possible
                        min_y = neighbor_y
                        min_x = neighbor_x

            return min_sub_path


    def v2(self, grid: List[List[int]], k: int) -> int:
        \"\"\"
        Nope, I suck. By using a visited set, I am now closing off paths that
        move BACKWARDS, but are valid. I guess I really do need to use a DFS
        after all.

        UPDATE: Nevermind, DFS runs into \"time limit exceeded.\" What I really
        should have done is also use \"destroyed\" as a key in the BFS
        implementation. Going back to using that.
        \"\"\"
        min_steps = self.dfs(grid, 0, 0, k, 0, [])

        if min_steps == float('inf'):
            return -1
        else:
            return min_steps


    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #return self.v0(grid, k)
        return self.v1(grid, k)
        #return self.v2(grid, k)

    def main(self):
        assert(self.shortestPath([
            [0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0],
        ], 1) == 6)

        assert(self.shortestPath([
            [0,1,1],
            [1,1,1],
            [1,0,0],
        ], 1) == -1)

        assert(self.shortestPath([
            [0,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [1,0],
            [0,0],
            [0,1],
            [0,1],
            [0,1],
            [0,0],
            [1,0],
            [1,0],
            [0,0]
        ], 4) == 14)

        assert(self.shortestPath([
            [0,1,0,0,0,1,0,0],
            [0,1,0,1,0,1,0,1],
            [0,0,0,1,0,0,1,0]
        ], 1) == 13)

