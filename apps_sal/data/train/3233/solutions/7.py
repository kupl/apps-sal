def robot_transfer(matrix, k):
    res = []
    for (r, rows) in enumerate(matrix):
        for (c, point) in enumerate(rows):
            kk = 1
            while kk <= k:
                t = list(map(int, point.split(',')))
                print(t)
                point = matrix[t[0]][t[1]]
                kk += 1
                if list(map(int, point.split(','))) == [r, c]:
                    break
            if kk == k and list(map(int, point.split(','))) == [r, c]:
                res.append(1)
    return sum(res)
