def main():
    n, aa = int(input()), [0, *list(map(int, input().split())), 0]
    l, clusters, mx = list(map(int, input().split())), [0] * (n + 2), 0
    for i in range(n - 1, -1, -1):
        a = clusters[a] = l[i]
        l[i] = mx
        for i in a - 1, a + 1:
            if clusters[i]:
                stack, j = [], i
                while j != clusters[j]:
                    stack.append(j)
                    j = clusters[j]
                for i in stack:
                    clusters[i] = j
                aa[a] += aa[j]
                clusters[j] = a
        if mx < aa[a]:
            mx = aa[a]
    print('\n'.join(map(str, l)))


def __starting_point():
    main()


__starting_point()
