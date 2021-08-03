def main():
    n, m = list(map(int, input().split()))

    r = []
    rappend = r.append
    for i in range(1, (n >> 1) + 1):
        for j in range(1, m + 1):
            rappend(str(i) + ' ' + str(j))
            rappend(str(n + 1 - i) + ' ' + str(m + 1 - j))

    if n & 1:
        for i in range(1, (m >> 1) + 1):
            rappend(str((n + 1) >> 1) + ' ' + str(i))
            rappend(str((n + 1) >> 1) + ' ' + str(m + 1 - i))
        if m & 1:
            rappend(str((n + 1) >> 1) + ' ' + str((m + 1) >> 1))

    print('\n'.join(r))


main()
