def dfs(ind, m, n):
    if(ind == m):
        return [""]
    else:
        temp = dfs(ind + 1, m, n)
        ans = []
        for i in temp:
            for j in range(97, 97 + n):
                ans += [chr(j) + i]
    return ans


n, m, k = list(map(int, input().split()))
p = []
for _ in range(m):
    inp = [int(x) for x in input().split()]
    p += [inp]
ans = dfs(0, m, n)
w = []
for i in ans:
    cst = 0
    for j in range(m):
        cst += p[j][ord(i[j]) - 97]
    w += [(-cst, i)]
w.sort()
print(w[k - 1][1])
