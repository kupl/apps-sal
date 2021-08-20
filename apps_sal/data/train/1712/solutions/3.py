def puzzle_solver(puzzle, w, h):
    sol = {}
    res = []
    p = {}
    for pc in puzzle:
        p[pc[0], pc[1][0]] = pc
    for j in range(h):
        rl = []
        for i in range(w):
            if i == 0:
                (lu, ld) = (None, None)
            else:
                lu = sol[i - 1, j][0][1]
                ld = sol[i - 1, j][1][1]
            if j == 0:
                ru = None
            else:
                ru = sol[i, j - 1][1][1]
            pc = p[(lu, ru), ld]
            sol[i, j] = pc
            rl.append(pc[2])
        res.append(tuple(rl))
    return res
