def n_closestPairs_tonum(num, k):
    result = []
    squares = []
    for i in range(1, (int)((2 * num) ** 0.5) + 2):
        squares.append(i ** 2)
    squares.reverse()
    for i in range(1, num):
        m = num - i
        np = []
        for s in squares:
            if s > m:
                np.append(s - m)
            else:
                break
        for n in np:
            if (m - n) in squares:
                result.append([m, n])
                if len(result) == k:
                    return result
