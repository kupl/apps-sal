for i in range(int(input())):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append([int(j) for j in input().split()])
    ans = 0
    t = True
    for i in range(n - 1, 0, -1):
        if t:
            if mat[0][i] != i + 1:
                t = False
                ans += 1
        elif mat[0][i] == i + 1:
            t = True
            ans += 1
    print(ans)
