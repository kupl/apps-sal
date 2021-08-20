for _ in range(int(input())):
    n = int(input())
    mat = []
    for x in range(n):
        mat.append([int(i) for i in input().split()])
    ans = [0] * n
    flag = True
    ans[-1] = max(mat[-1])
    for i in range(n - 2, -1, -1):
        for ele in mat[i]:
            if ele < ans[i + 1]:
                ans[i] = max(ans[i], ele)
        if ans[i] == 0:
            flag = False
            break
    if flag:
        print(sum(ans))
    else:
        print(-1)
