def count_sheep(n):
    z = 1
    sheeps = ""
    while z <= n :
        sheep = f"{z} sheep..."
        sheeps = sheeps + sheep
        z += 1
    return sheeps
