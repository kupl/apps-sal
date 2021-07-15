# cook your dish here
for _ in range(int(input())):
    n, r = map(int, input().split())
    reg_teams = [input().split() for _ in range(r)]
    after = [input().split() for _ in range(n - r)]
    check1 = [[''.join(sorted(list(s))), int(p), s] for s, p in reg_teams]
    check2 = {}
    for a in after:
        cur = "".join(sorted(list(a[0])))
        if cur in check2.keys():
            check2[cur] += int(a[1])
        else:
            check2[cur] = int(a[1])
    for c in check1:
        if c[0] in check2.keys():
            c[1] += check2[c[0]]

    check1.sort(key = lambda z: z[2])
    check1.sort(key = lambda z: z[1], reverse = True)
    for c in check1:
        print(c[2], c[1])
