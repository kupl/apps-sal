from itertools import permutations
C = list(permutations(['A', 'B', 'C', 'D']))
V = list(permutations([3, 6, 9, 12]))
P = list(permutations([25, 50, 75, 100]))
R = []


def test():
    d = {}
    n = int(input())
    for i in C[0]:
        for j in V[0]:
            d[i + str(j)] = 0
    for i in range(n):
        (x, y) = input().split()
        d[x + y] += 1
    ans = -1000000000
    for i in C:
        for j in V:
            for k in P:
                c = 0
                for l in range(4):
                    if d[i[l] + str(j[l])] == 0:
                        c -= 100
                    else:
                        c += d[i[l] + str(j[l])] * k[l]
                ans = max(ans, c)
    R.append(ans)
    print(ans)


def __starting_point():
    t = int(input())
    for i in range(t):
        test()
    print(sum(R))


__starting_point()
