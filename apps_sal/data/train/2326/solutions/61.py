def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {0: [-1]}
    for (j, i) in enumerate(a):
        if i in d.keys():
            d[i].append(j)
        else:
            d[i] = [j]
    d = sorted([[i, min(j), len(j)] for (i, j) in d.items()], reverse=True)
    ans = [0] * n
    l = 0
    m = n
    for k in range(len(d) - 1):
        (x, y, z) = d[k]
        l += z
        m = min(m, y)
        ans[m] += (x - d[k + 1][0]) * l
    for i in ans:
        print(i)


main()
