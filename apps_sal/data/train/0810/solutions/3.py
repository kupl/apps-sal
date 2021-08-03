for _ in range(int(input())):
    n, q = map(int, input().split())

    a = list(map(int, input().split()))

    for _ in range(q):
        b = list(map(int, input().split()))
        if b[0] == 0:
            a[b[1]] = b[2]

        if b[0] == 1:
            ans = -1
            for i in range(b[1] + 1, n):
                if a[i] > a[b[1]] and (a[i] not in a[:b[1]]):
                    ans = a[i]
                    break

            print(ans)
