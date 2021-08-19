def path_finder(maze):
    mtx = list(map(list, maze.splitlines()))
    R = len(mtx[0])
    mtx[R - 1][R - 1] = 'E'
    (sr, sc) = (0, 0)
    (rq, cq) = ([], [])
    prev = [[' '] * R for x in range(R)]
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    reached_end = False
    visited = [[False] * R for x in range(R)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while len(rq):
        r = rq.pop(0)
        c = cq.pop(0)
        if mtx[r][c] == 'E':
            reached_end = True
            return move_count
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr < 0 or cc < 0:
                continue
            if rr >= R or cc >= R:
                continue
            if visited[rr][cc]:
                continue
            if mtx[rr][cc] == 'W':
                continue
            rq.append(rr)
            cq.append(cc)
            visited[rr][cc] = True
            prev[rr][cc] = [r, c]
            nodes_in_next_layer += 1
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    else:
        return False
