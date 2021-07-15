def not_visible_cubes(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    totalCubes = n*n*n
    cubesPerSide = n*n
    outsideCubes = cubesPerSide + 2*(cubesPerSide - n) + cubesPerSide - 2*n + 2*(cubesPerSide - (n + 2*(n - 1) + n - 2))
    return totalCubes - outsideCubes
