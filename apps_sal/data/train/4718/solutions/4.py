def x(n):
    zarr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        zarr[i][i] = 1
        zarr[i][-(i + 1)] = 1
    return zarr
