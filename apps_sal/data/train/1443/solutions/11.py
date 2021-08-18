
def collisions(ar, n, m):
    res = 0
    for i in range(m):
        tem1, tem2 = 0, 0
        for j in range(n):
            if ar[j][i] == '1':
                tem1 += tem2
                tem2 += 1
        res += tem1
    return res


def __starting_point():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        ar = []
        for i in range(n):
            ar.append(list(input()))
        print(collisions(ar, n, m))


__starting_point()
