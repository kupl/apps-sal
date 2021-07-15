for q in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    G = {}
    for i in A:
        if i not in G:
            G[i] = 0
        G[i] += 1
    B = []
    for i in G:
        B.append(G[i])
    B.sort(reverse=True)
    cnt = 0
    op = B[0] + 1
    for i in B:
        if i >= op:
            op -= 1
            cnt += max(0, op)
        else:
            op = i
            cnt += i
        if op == 0:
            break
    print(cnt)
