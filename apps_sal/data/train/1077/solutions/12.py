cases = int(input())
for case in range(cases):
    N = int(input())
    A = []
    B = []
    for n in range(N):
        x, y = input().split(" on ")
        A.append(x)
        B.append(y)
    x = n
    y = n - 1
    print(A[0], 'on', B[n])
    for y in range(N - 1, 0, -1):
        if (A[x] == "Right"):
            print("Left on", B[y - 1])
        else:
            print("Right on", B[y - 1])
        x -= 1
    if (case != cases - 1):
        print("")
