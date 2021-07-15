def has_two_cube_sums(n):
    x = 0
    for a in range(int(n**0.35)):
        for b in range(a,int(n**0.35)):
            if a**3+b**3 == n:
                x += 1
            if x > 1:
                return True
    return False

