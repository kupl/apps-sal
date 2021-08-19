from collections import deque


# class Node:
#     def __init__(self, row, col):
#         self.row = row
#         self.col = col
#         self.k_used = 0
#         self.steps_taken = -1
#         self.discovered = False

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:  # if only one node then we don't need to move
            return 0

        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        # why do we need 2 separate queues?

        while queue:
            row, col, eliminate, steps = queue.popleft()
            for new_row, new_col in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:  # clean way to handle long if statement
                if (new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0])):
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate - 1) not in visited:
                        visited.add((new_row, new_col, eliminate - 1))
                        queue.append((new_row, new_col, eliminate - 1, steps + 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                            return steps + 1
                        visited.add((new_row, new_col, eliminate))
                        queue.append((new_row, new_col, eliminate, steps + 1))

        return -1


# grid =
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]],

# breadth first search to find distance of each node from upper left
# keep track of number of obstacles eliminated
# if num of obstacles eliminated == k or reached ending, then that node has no edges

# question: do we need to revisit a node we reached before? yes if k < prev_k when we previously reached that node

# what do we store in the bfs search? indices, k, dist, steps from upper left
# how to remember that we traversed a node? #initialize this

#         grid_info = []
#         for row in range(len(grid)):
#             grid_info.append([])
#             for col in range(len(grid[0])): #assume we have at least 1 row
#                 grid_info[row].append(Node(row, col))

#         grid_info[0][0].steps_taken = 0
#         grid_info[0][0].discovered = True

#         queue = deque([grid_info[0][0]]) #assume we don't start at obstacle
#         while len(queue) > 0:
#             cur_node = queue.popleft()
#             if cur_node.row > 0:
#                 up_node = grid_info[cur_node.row - 1][cur_node.col]
#                 self.check_and_add_to_queue(queue, cur_node, up_node, k, grid)
#             if cur_node.row < len(grid) - 1:
#                 down_node = grid_info[cur_node.row + 1][cur_node.col]
#                 self.check_and_add_to_queue(queue, cur_node, down_node, k, grid)
#             if cur_node.col > 0:
#                 left_node = grid_info[cur_node.row][cur_node.col - 1]
#                 self.check_and_add_to_queue(queue, cur_node, left_node, k, grid)
#             if cur_node.col < len(grid[0]) - 1:
#                 right_node = grid_info[cur_node.row][cur_node.col + 1]
#                 self.check_and_add_to_queue(queue, cur_node, right_node, k, grid)

#         return grid_info[len(grid) - 1][len(grid[0]) -1 ].steps_taken

#     def check_and_add_to_queue(self, queue, cur_node, new_node, k, grid):
#         if (not new_node.discovered and ((grid[new_node.row][new_node.col] == 0 and cur_node.k_used <= k) or (grid[new_node.row][new_node.col] == 1 and cur_node.k_used + 1 <= k))) or (grid[new_node.row][new_node.col] == 0 and cur_node.k_used < new_node.k_used) or grid[new_node.row][new_node.col] == 1 and cur_node.k_used + 1 < new_node.k_used:
#             queue.append(new_node)
#             new_node.discovered = True
#             if grid[new_node.row][new_node.col] == 1:
#                 new_node.k_used = cur_node.k_used + 1
#             else:
#                 new_node.k_used = cur_node.k_used
#             new_node.steps_taken = cur_node.steps_taken + 1
