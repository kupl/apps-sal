import typing as t
import heapq


class Solution:
    def shortestBridge(self, A: t.List[t.List[int]]) -> int:
        dist_arr: t.Dict[t.Tuple[int, int], float] = {}
        heap: t.List[t.Tuple[float, t.Tuple[int, int]]] = []

        row_limit = len(A)
        col_limit = len(A[0])
        first_one_found = False
        for i in range(row_limit):
            for j in range(col_limit):
                distance = float(\"inf\")
                if A[i][j] == 1 and first_one_found is False:
                    distance = 0
                    first_one_found = True
                    heapq.heappush(heap, (distance, (i, j)))
                dist_arr[(i, j)] = distance

        min_dist = float(\"inf\")
        while heap:
            current_dist, (i, j) = heapq.heappop(heap)
            if A[i][j] == 1 and current_dist > 0:
                min_dist = min(min_dist, current_dist)
            for x_offset, y_offset in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                new_i, new_j = i + x_offset, j + y_offset
                if new_i < 0 or new_i >= row_limit or new_j < 0 or new_j >= col_limit:
                    continue
                if A[new_i][new_j] == 1:
                    new_dist = current_dist
                else:
                    new_dist = current_dist + 1
                if new_dist < dist_arr[(new_i, new_j)]:
                    dist_arr[(new_i, new_j)] = new_dist
                    heapq.heappush(heap, (new_dist, (new_i, new_j)))
            # print(f\"{heap=}, {current_dist=}, {i=}, {j=}\")
        return int(min_dist)
