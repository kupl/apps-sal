def main():

    from bisect import bisect_left as bl

    n = int(input())
    a = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in [0]*(n-1)]
    g = [set() for _ in [0]*n]
    ans = [0]*n
    [g[a-1].add(b-1) for a, b in ab]
    [g[b-1].add(a-1) for a, b in ab]
    visited = [False]*n

    q = [0]
    lis = []
    while q:
        i = q.pop()
        ai = a[i]
        if not visited[i]:
            b = bl(lis, ai)
            if b == len(lis):
                visited[i] = "push"
                lis.append(ai)
            else:
                visited[i] = [b, lis[b]]
                lis[b] = ai
            ans[i] = len(lis)
        if not g[i]:
            if visited[i] == "push":
                lis.pop()
            else:
                lis[visited[i][0]] = visited[i][1]
        else:
            q.append(i)
            j = g[i].pop()
            g[j].remove(i)
            q.append(j)
    for i in ans:
        print(i)


main()
