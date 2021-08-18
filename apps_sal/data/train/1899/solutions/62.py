import numpy as np


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.R, self.C = len(A), len(A[0])
        self.queue = []
        self.visited = []
        for k in range(self.R):
            self.visited.append([0] * self.C)

        count = 0

        for rr in range(self.R):
            for cc in range(self.C):
                if A[rr][cc] == 1:
                    self.dfs(A, rr, cc)
                    count = 1
                if count > 0:
                    break
            if count > 0:
                break

        while self.queue:
            node_visit = self.queue.pop(0)
            q_step = node_visit.step

            for r_srch, c_srch in self.dirs(A, node_visit.r, node_visit.c):
                if A[r_srch][c_srch] == 0 and self.visited[r_srch][c_srch] == 0:
                    self.queue.append(self.node(q_step + 1, r_srch, c_srch))
                    self.visited[r_srch][c_srch] = 1
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
        self.queue.append(self.node(0, r, c))
        self.visited[r][c] = 1

        for r_srch, c_srch in self.dirs(A, r, c):
            self.dfs(A, r_srch, c_srch)

    class node:
        def __init__(self, step, r, c):
            self.step = step
            self.r = r
            self.c = c
