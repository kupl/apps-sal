def count_sheep(n):
    sheep = " sheep..."
    newStr = ""
    for i in range(1, n + 1):
        newStr += str(i) + sheep

    return newStr
