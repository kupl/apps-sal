def longest_slide_down(pyramid):
    l = len(pyramid)
    for i in range(l-2,-1,-1):
        for j in range(i+1):
            pyramid[i][j] = max([pyramid[i+1][j],pyramid[i+1][j+1]])+pyramid[i][j]
    return pyramid[0][0]

