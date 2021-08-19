for _ in range(int(input())):
    n = int(input())
    a = list(input())
    n1 = []
    n0 = []
    ans = []
    c1 = 0
    c0 = 0
    curr = 1
    for i in a:
        if i == '1':
            if c0 > 0:
                c1 += 1
                c0 -= 1
                ans.append(n0[-1])
                n1.append(n0[-1])
                n0.pop()
            else:
                c1 += 1
                ans.append(curr)
                n1.append(curr)
                curr += 1
        elif c1 > 0:
            c0 += 1
            c1 -= 1
            ans.append(n1[-1])
            n0.append(n1[-1])
            n1.pop()
        else:
            c0 += 1
            ans.append(curr)
            n0.append(curr)
            curr += 1
    print(c1 + c0)
    print(*ans)
