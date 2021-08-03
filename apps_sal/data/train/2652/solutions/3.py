def count_squares(lines):
    print('\n'.join(lines))
    tot = 0
    for l in range(len(lines)):
        for i in range(len(lines[l]) - 1):
            if lines[l][i] != '+':
                continue
            for j in range(i + 1, len(lines[l])):
                if lines[l][j] == '+':
                    try:
                        n = j - i
                        if lines[l + n][i] == '+' == lines[l + n][j] \
                                and all(lines[m][i] not in ' -' for m in range(l + 1, l + n)) \
                                and all(lines[m][j] not in ' -' for m in range(l + 1, l + n)) \
                                and all(lines[l][m] not in ' |' for m in range(i + 1, j)) \
                                and all(lines[l + n][m] not in ' |' for m in range(i + 1, j)):
                            tot += 1
                    except:
                        pass
    return tot
