def checkered_board(n):
    if type(n) != int or n < 2:
        return False
    return "\n".join(" ".join("□■"[(i + j + n) % 2] for j in range(n)) for i in range(n))
