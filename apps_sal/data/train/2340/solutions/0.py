t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    cur = l[0]
    cll = 1
    blocks = []
    for x in l[1:]:
        if x > cur:
            blocks.append(cll)
            cur = x
            cll = 1
        else:
            cll += 1
    blocks.append(cll)

    poss = [[False]*(n+1) for _ in range(len(blocks) + 1)]
    poss[0][0] = True
    for i, b in enumerate(blocks):
        for j in range(n+1):
            poss[i+1][j] = poss[i][j]
            if b <= j:
                poss[i+1][j] |= poss[i][j-b]

    # print()
    # print(blocks)
    # for r in poss:
    #     print(r)
    print("YES" if poss[len(blocks)][n] else "NO")

