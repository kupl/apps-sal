def amazon_check_mate(k, q):
    import numpy
    board = numpy.array([[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                         [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                         [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 1, 1],
                         [0, 0, 0, 0, 0, 0, -1, -2, -1, 0, 0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                         [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                         [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]])

    qx, qy = ord(q[0]) - 97, int(q[1]) - 1
    kx, ky = ord(k[0]) - 97, int(k[1]) - 1
    board[max(0, 6 + qy - ky):9 + qy - ky, max(0, 6 - qx + kx):9 - qx + kx] = -2
    board = board[qy:qy + 8, 7 - qx:15 - qx]

    if abs(qx - kx) > 1 or abs(qy - ky) > 1:
        board[board == -1] = 0
        board[7 - qy, qx] = 2
    if qy == ky:
        if kx + 2 - (qx > kx) * 4 >= 0:
            board[7 - ky, kx + 2 - (qx > kx) * 4::1 - (qx > kx) * 2] = 1
    elif qx == kx:
        if 7 - ky - 2 + (qy > ky) * 4 >= 0:
            board[7 - ky - 2 + (qy > ky) * 4::-1 + (qy > ky) * 2, kx] = 1
    elif kx + ky == qx + qy:
        newb = board[7 - ky::1 - (qx > kx) * 2, kx::1 - (qx > kx) * 2]
        newb[newb == 0] = 1
        board[7 - ky::1 - (qx > kx) * 2, kx::1 - (qx > kx) * 2] = newb
    elif kx - ky == qx - qy:
        newb = board[7 - ky::-1 + (qx > kx) * 2, kx::1 - (qx > kx) * 2]
        newb[newb == 0] = 1
        board[7 - ky::-1 + (qx > kx) * 2, kx::1 - (qx > kx) * 2] = newb

    ans = [0, 0, 0, 0]
    ansb = numpy.empty(shape=(8, 8), dtype=object)
    for nx in range(8):
        for ny in range(8):
            c = board[7 - ny, nx]
            if c == 1:
                pos = numpy.count_nonzero(board[max(0, 6 - ny):9 - ny, max(0, nx - 1):nx + 2] > 0) - 1
                if pos:
                    ans[3] += 1
                    ansb[7 - ny, nx] = "o"
                else:
                    ans[2] += 1
                    ansb[7 - ny, nx] = "□"
            elif c == 0:
                pos = numpy.count_nonzero(board[max(0, 6 - ny):9 - ny, max(0, nx - 1):nx + 2] > 0)
                if pos:
                    ans[1] += 1
                    ansb[7 - ny, nx] = "+"
                else:
                    ans[0] += 1
                    ansb[7 - ny, nx] = "x"
            elif c == -1:
                ans[0] += 1
                ansb[7 - ny, nx] = "x"
            else:
                ansb[7 - ny, nx] = " "
    print(k, q)
    print(board)
    print(ans)
    print(ansb)
    return ans
