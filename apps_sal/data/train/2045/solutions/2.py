def main():
    mode = "filee"
    if mode == "file":
        f = open("test.txt", "r")

    def get(): return [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    [n, m] = get()
    k = [0 for i in range(n)]
    g = [z + 1 for z in range(n + 1)]
    for i in range(m):
        [m, n, p] = get()
        j = m - 1
        while j <= n - 1:
            if k[j] == 0 and j != p - 1:
                k[j] = p
            tmp = g[j]
            if j < p - 1:
                g[j] = p - 1
            else:
                g[j] = n
            # print(j+1,tmp,g[j])
            j = tmp
    for i in k:
        print(i, end=' ')

    if mode == "file":
        f.close()


def __starting_point():
    main()
# copied...


__starting_point()
