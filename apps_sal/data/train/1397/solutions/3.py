t = int(input())
for j in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = list(set(l))
    s.sort()
    dic = {}
    le = {}
    for j in s:
        dic[j] = []
        le[j] = 0
    for j in range(n):
        dic[l[j]].append(j + 1)
        le[l[j]] += 1
    stack = [dic[s[0]][0]]
    z = 0
    m = 1
    x = len(s)
    for j in range(1, x):
        flag = 0
        for k in range(le[s[j]]):
            if dic[s[j]][k] + (m - 1) * n > stack[z]:
                stack.append(dic[s[j]][k] + (m - 1) * n)
                z += 1
                flag = 1
                break
        if flag == 0:
            m += 1
            stack.append(dic[s[j]][0] + (m - 1) * n)
            z += 1
    print(m)
