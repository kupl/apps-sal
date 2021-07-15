import heapq
from typing import List


class Solution:
  def minimumMoves(self, grid: List[List[int]]) -> int:

    self.grid = grid
    self.R, self.C = len(grid), len(grid[0])
    target = (self.R - 1, self.C - 1)

    q = [(0, 0, 1, 0)]  # (distance traveled, row, column, orientation)
    visited = [{(0, 1): 0}, {}]  # visited in horizontal state, visited in vertical state

    while q:

      d, r, c, o = heapq.heappop(q)

      # Check if snake can shift down, shift right, or rotate
      shift_d, shift_r, rot = self.shift_down(r, c, o), self.shift_right(r, c, o), self.rotate(r, c, o)

      # increment distance traveled by 1
      d += 1

      # Update the queue and visited after the snake has shifted down, right, or rotated
      if shift_d:
        i, j = shift_d
        if d < visited[o].get((i, j), float('inf')):
          visited[o][(i, j)] = d
          heapq.heappush(q, (d, i, j, o))

      if shift_r:
        i, j = shift_r
        if d < visited[o].get((i, j), float('inf')):
          visited[o][(i, j)] = d
          heapq.heappush(q, (d, i, j, o))

      if rot:
        i, j = rot
        if d < visited[1 - o].get((i, j), float('inf')):
          visited[1 - o][(i, j)] = d
          heapq.heappush(q, (d, i, j, 1 - o))

    return visited[0].get(target, -1)

  def shift_right(self, r, c, orient):
    '''returns False if snake cannot move to the right, otherwise returns new head position'''
    if (orient == 0) and ((c == self.C - 1) or self.grid[r][c + 1]): return False
    if (orient == 1) and ((c == self.C - 1) or self.grid[r][c + 1] or self.grid[r - 1][c + 1]): return False
    return (r, c + 1)

  def shift_down(self, r, c, orient):
    '''returns False if snake cannot move downwards, otherwise returns new head position'''
    if (orient == 1) and ((r == self.R - 1) or self.grid[r + 1][c]): return False
    if (orient == 0) and ((r == self.R - 1) or self.grid[r + 1][c] or self.grid[r + 1][c - 1]): return False
    return (r + 1, c)

  def rotate(self, r, c, orient):
    '''returns False if the snake is blocked from rotating, otherwise returns new head position (r,c)'''
    # horizontal to vertical CW rotation
    if (orient == 0) and ((r == self.R - 1) or self.grid[r + 1][c] or self.grid[r + 1][c - 1]): return False
    if (orient == 0): return (r + 1, c - 1)

    # vertical to horizontal CCW rotation
    if (c == self.C - 1) or self.grid[r][c + 1] or self.grid[r - 1][c + 1]: return False
    return (r - 1, c + 1)

