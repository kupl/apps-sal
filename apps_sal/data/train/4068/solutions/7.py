def get_candy_position(n, r, c, candy):
    if min(n, r, c, candy) <= 0 or candy > n:
        return [-1] * 3
    box, candy = divmod(candy - 1, r * c)
    row, col = divmod(candy, c)
    return [box + 1, r - row - 1, c - col - 1]
