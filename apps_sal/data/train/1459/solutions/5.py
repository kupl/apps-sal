from math import sqrt
(N, M) = input().split()
(N, M) = (int(N), float(M))
if M == 0:
    n = 0
    while n < N:
        (xi, yi) = input().split()
        (xi, yi) = (float(xi), float(yi))
        if n == 0:
            c1_min = c1_max = xi
            c2_min = c2_max = yi
        else:
            if c1_min > xi:
                c1_min = xi
            elif c1_max < xi:
                c1_max = xi
            if c2_min > yi:
                c2_min = yi
            elif c2_max < yi:
                c2_max = yi
        n += 1
    perimeter = 2 * (c2_max - c2_min + c1_max - c1_min)
else:
    n = 0
    while n < N:
        (xi, yi) = input().split()
        (xi, yi) = (float(xi), float(yi))
        temp1 = yi - M * xi
        temp2 = yi + xi / M
        if n == 0:
            c1_min = c1_max = temp1
            c2_min = c2_max = temp2
        else:
            if c1_min > temp1:
                c1_min = temp1
            elif c1_max < temp1:
                c1_max = temp1
            if c2_min > temp2:
                c2_min = temp2
            elif c2_max < temp2:
                c2_max = temp2
        n += 1
    perimeter = 2 * ((c1_max - c1_min) / sqrt(1.0 + M * M) + (c2_max - c2_min) / sqrt(1.0 + 1.0 / (M * M)))
print(perimeter)
