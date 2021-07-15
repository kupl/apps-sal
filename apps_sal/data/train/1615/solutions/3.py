def longest_slide_down(pyramid):
    i = len(pyramid) - 2
    while i > - 1:
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
        i -= 1
    return pyramid[0][0]
