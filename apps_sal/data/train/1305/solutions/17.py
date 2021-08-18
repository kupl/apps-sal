t = int(input())

for xx in range(t):
    n = int(input())

    A = []

    for i in range(n):
        A.append([int(x) for x in input().split()])

    check = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                if i < n - 1 and A[i + 1][j] == 1:
                    check = 1
                    break
                elif j < n - 1 and A[i][j + 1] == 1:
                    check = 1
                    break
        if check == 1:
            break

    if check == 0:
        print("SAFE")
    else:
        print("UNSAFE")
