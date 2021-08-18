def check_For_L(i, n, counter):
    if counter & 1:
        if matrix[0][i] != i * n + 1:
            return False
    elif matrix[i][0] != i * n + 1:
        return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    matrix = []
    for j in range(N):
        matrix.append(list(map(int, input().split())))
    counter = 0

    for j in reversed(list(range(N))):
        if check_For_L(j, N, counter):
            continue
        else:
            counter += 1

    print(counter)
