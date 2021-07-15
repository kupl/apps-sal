def count_sheep(n):
    sheep = ""
    x = 1
    while x <= n :
        sheep = sheep + str(x) + " sheep..."
        x += 1
    return sheep
