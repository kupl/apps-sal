class Solution:
    def shortestPath(self, map: List[List[int]], k: int) -> int:
        import collections
        h, w = len(map), len(map[0])

        def check_map(i, j, rw):
            if i >= h or i < 0: return 1
            if j >= w or j < 0: return 1
            if map[i][j] == 1 and rw > 0: return -1
            if map[i][j] == 1 and rw == 0: return 1

            return 0

                   # i    j    st rw
        start_pos = (0, 0, 0, k)
        q = collections.deque([])
        q.append(start_pos)
        seen = set()
        seen.add((0, 0, k))
        # vis[h-1][w-1]= \"X\"
        while q:
            # print(\"Q\",q)

            i, j, step, rw = q.popleft()
            if i == h - 1 and j == w - 1:
                return step

            fw = [i - 1, j]
            bw = [i + 1, j]
            lf = [i, j - 1]
            rt = [i, j + 1]

            moves = [bw, rt, lf, fw]

    #         print(moves)
            for move in moves:
                ni, nj = move
                # print(\">\",move)
                map_state = check_map(ni, nj, rw)
                if map_state in (0, -1) and (ni, nj, rw + map_state) not in seen:
                    # if map_state == -1:
                    # print(map_state)
                    q.append([ni, nj, step + 1, rw + map_state])
                    seen.add((ni, nj, rw + map_state))
        return -1
