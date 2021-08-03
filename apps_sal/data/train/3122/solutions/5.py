
KNIGHTX = [1, 2, 2, 1, -1, -2, -2, -1]
KNIGHTY = [2, 1, -1, -2, -2, -1, 1, 2]


def chess_triangle(n, m):
    result = 0
    for bishopx, bishopy in zip(KNIGHTX, KNIGHTY):
        for rookx, rooky in [(0, bishopx + bishopy), (0, bishopy - bishopx), (bishopx + bishopy, 0), (bishopx - bishopy, 0)]:
            result += max(0, n - (max(bishopx, rookx, 0) - min(bishopx, rookx, 0))) * max(0, m - (max(bishopy, rooky, 0) - min(bishopy, rooky, 0)))
    for rookx, rooky in zip(KNIGHTX, KNIGHTY):
        for bishopx, bishopy in [(rookx, rookx), (rookx, -rookx), (rooky, rooky), (-rooky, rooky)]:
            result += max(0, n - (max(bishopx, rookx, 0) - min(bishopx, rookx, 0))) * max(0, m - (max(bishopy, rooky, 0) - min(bishopy, rooky, 0)))
    return result
