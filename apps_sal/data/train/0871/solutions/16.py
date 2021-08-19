for _ in range(int(input())):
    r, c = map(int, input().split())
    m = [[*input()] for _ in range(r)]

    ans = 0
    p = []

    for i in range(r):
        for j in range(c):
            if m[i][j] in 'UDLR':
                p.append([i, j, m[i][j]])

    from collections import Counter

    for i in range(max(r, c) + 1):
        z = Counter([tuple(i[:2]) for i in p])
        for j in z.values():
            ans += (j * (j - 1)) // 2

        d = set()

        for j in range(len(p)):
            if p[j][2] == 'U':
                if p[j][0] > 0 and m[p[j][0] - 1][p[j][1]] != '#':
                    p[j][0] -= 1
                else:
                    d.add(j)
            elif p[j][2] == 'R':
                if p[j][1] < c - 1 and m[p[j][0]][p[j][1] + 1] != '#':
                    p[j][1] += 1
                else:
                    d.add(j)
            elif p[j][2] == 'L':
                if p[j][1] > 0 and m[p[j][0]][p[j][1] - 1] != '#':
                    p[j][1] -= 1
                else:
                    d.add(j)
            else:
                if p[j][0] < r - 1 and m[p[j][0] + 1][p[j][1]] != '#':
                    p[j][0] += 1
                else:
                    d.add(j)

        p = [p[i] for i in set([*range(len(p))]) - d]

    print(ans)
