def least_bribes(bribes):
    # worst[k][i] is the minimal amount of bribes spent in the worst case
    # for a subarray of length k beginning at index i.
    worst = [[0] * (len(bribes) + 1)]
    for k in range(1, len(bribes) + 1):
        #worst.append([min(bribes[j] + max(worst[j-i][i], worst[i+k-j-1][j+1]) for j in range(i, i + k)) for i in range(len(bribes) - k + 1)])
        worst.append([min(bribes[i+j] + max(worst[j][i], worst[-j-1][i+j+1]) for j in range(k)) for i in range(len(bribes) - k + 1)])
    return worst[-1][-1]
