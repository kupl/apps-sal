def points(radius):
    cnt = radius * 4 + 1
    r2 = radius * radius
    for i in range(1, radius + 1):
        for j in range(1, radius + 1):
            if (i * i + j * j <= r2):
                cnt += 4
    return cnt
