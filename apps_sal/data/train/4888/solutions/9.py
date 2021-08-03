R = [0]
for i in range(1, 30000):
    if R[i - 1] - i > 0 and R[i - 1] - i not in R:
        R.append(R[i - 1] - i)
    else:
        R.append(R[i - 1] + i)


def recaman(n):
    return R[n]
