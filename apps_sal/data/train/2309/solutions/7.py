visited = [-1] * (2 * 10 ** 6 + 1)
t = int(input())
for i in range(t):
    n, A = int(input()), list(map(int, input().split()))
    A.sort()
    res = []
    v = 1
    while len(res) < n:
        flag = True
        for a in A:
            if visited[a + v] == i:
                flag = False
                break
        if not flag:
            v += 1
            continue
        for a in A:
            visited[a + v] = i
        res.append(v)
        v += 1
    print("YES\n" + ' '.join(map(str,res)))

