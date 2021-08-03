S = input()
N = len(S)
Q = int(input())
A = [[0] * 27 for i in range(N)]
for i in range(N):
    try:
        if i > 0:
            for j in range(1, 27):
                A[i][j] = A[i - 1][j]
        A[i][ord(S[i]) - ord('a') + 1] += 1
    except:
        pass
# for i in A:
#     print(i)
while Q > 0:
    Q -= 1
    X, Y = [int(x) for x in input().split()]
    ans = 0
    X -= 1
    Y -= 1
    for i in range(2, 27, 2):
        try:
            if X > 0:
                val = A[Y][i] - A[X - 1][i]
            else:
                val = A[Y][i]
        except:
            pass
        if (val) > 0:
            ans += 1
    print(ans)
