for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [x for x in input().split()]
    s = set()
    for i in range(k):
        for w in input().split():
            s.add(w)
    ans = []
    for i in range(n):
        ans.append('YES') if a[i] in s else ans.append('NO')
    print(' '.join(ans))
