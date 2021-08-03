n = int(input())
for _ in range(n):
    a = int(input())
    l = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    s1 = 0
    s2 = 0
    ans = 0
    for i in range(a):
        if l[i] == l1[i] and s1 == s2:
            s1 += l[i]
            s2 += l1[i]
            ans += l[i]
        else:
            s1 += l[i]
            s2 += l1[i]
    print(ans)
