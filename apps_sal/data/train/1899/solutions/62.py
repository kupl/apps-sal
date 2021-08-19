import numpy as np


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.R, self.C = len(A), len(A[0])
        self.queue = []   # implement queue as list
        # self.visited = [[0]*self.C]*self.R  # weird construction doesn't work quite right
        self.visited = []
        for k in range(self.R):
            self.visited.append([0] * self.C)

        count = 0

        for rr in range(self.R):
            for cc in range(self.C):
                if A[rr][cc] == 1:
                    self.dfs(A, rr, cc)
                    count = 1
                if count > 0:  # break out of for-loop to get just first island
                    break
            if count > 0:
                break

        while self.queue:  # bfs
            node_visit = self.queue.pop(0)  # pop first element from queue
            q_step = node_visit.step

            for r_srch, c_srch in self.dirs(A, node_visit.r, node_visit.c):
                if A[r_srch][c_srch] == 0 and self.visited[r_srch][c_srch] == 0:
                    self.queue.append(self.node(q_step + 1, r_srch, c_srch))
                    self.visited[r_srch][c_srch] = 1  # forgot this in first submission
                if A[r_srch][c_srch] == 1:
                    return q_step

    def dirs(self, A, r, c) -> int:
        dir_list = []
        for rr, cc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
            if rr >= 0 and cc >= 0 and rr < self.R and cc < self.C:
                dir_list.append([rr, cc])
        return dir_list

    def dfs(self, A, r, c):
        if A[r][c] != 1:
            return
        A[r][c] = 2
        self.queue.append(self.node(0, r, c))  # adding nodes to queue for bfs
        self.visited[r][c] = 1  # visited by dfs

        for r_srch, c_srch in self.dirs(A, r, c):
            self.dfs(A, r_srch, c_srch)

    class node:
        def __init__(self, step, r, c):
            self.step = step
            self.r = r
            self.c = c
