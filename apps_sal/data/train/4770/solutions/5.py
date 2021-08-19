def peak_height(mountain):
    new_mnt = [['x' for i in range(len(mountain[0]))] for _ in range(len(mountain))]
    for i in range(len(mountain)):
        for j in range(len(mountain[0])):
            if mountain[i][j] == '^':
                if i > 0 and j > 0 and (i < len(mountain) - 1) and (j < len(mountain[0]) - 1):
                    if mountain[i + 1][j] == ' ' or mountain[i - 1][j] == ' ' or mountain[i][j + 1] == ' ' or (mountain[i][j - 1] == ' '):
                        new_mnt[i][j] = 1
                else:
                    new_mnt[i][j] = 1
            else:
                new_mnt[i][j] = 0
    done = False
    round = 1
    while not done:
        done = True
        for i in range(0, len(new_mnt) - 1):
            for j in range(0, len(new_mnt[0]) - 1):
                if new_mnt[i][j] == 'x':
                    if new_mnt[i + 1][j] == round or new_mnt[i - 1][j] == round or new_mnt[i][j + 1] == round or (new_mnt[i][j - 1] == round):
                        new_mnt[i][j] = round + 1
                    else:
                        done = False
        round += 1
    maxVal = 0
    for l in new_mnt:
        maxVal = max(maxVal, max(l))
    return maxVal
