from heapq import heappush, heappop


class Solution:

    def minPushBox(self, A: List[List[str]]) -> int:
        (m, n) = (len(A), len(A[0]))
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'B':
                    b_pos = (i, j)
                elif A[i][j] == 'T':
                    t_pos = (i, j)
                elif A[i][j] == 'S':
                    p_pos = (i, j)

        def estimate(pos):
            return abs(t_pos[0] - pos[0]) + abs(t_pos[1] - pos[1])
        seen = {(p_pos, b_pos)}
        heap = [[estimate(b_pos), 0, p_pos, b_pos]]
        nbs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while heap:
            (est, cost, person, box) = heappop(heap)
            if box == t_pos:
                return cost
            for (a, b) in nbs:
                (x, y) = (person[0] + a, person[1] + b)
                if 0 <= x < m and 0 <= y < n and (A[x][y] != '#'):
                    n_person = (x, y)
                    n_box = box
                    n_cost = cost
                    if n_person == box:
                        n_box = (x + a, y + b)
                        n_cost += 1
                    if 0 <= n_box[0] < m and 0 <= n_box[1] < n and (A[n_box[0]][n_box[1]] != '#') and ((n_person, n_box) not in seen):
                        heappush(heap, [estimate(n_box) + n_cost, n_cost, n_person, n_box])
                        seen.add((n_person, n_box))
        return -1
