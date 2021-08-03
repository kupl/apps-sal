def longest_slide_down(pyr):
    for row in range(len(pyr) - 1, 0, -1):
        for col in range(0, row):
            pyr[row - 1][col] += max(pyr[row][col], pyr[row][col + 1])
    return pyr[0][0]
