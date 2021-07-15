def has_two_cube_sums(n):
    return len([[y,z] for y in range(1, int(n**(1/3))+1) for z in [x for x in range(1, int(n**(1/3))+1)] if y!=z and y**3+z**3==n])>=4
