for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    s = set()
    for i in range(0, n - 1):
        for k in range(1, n):

            x = 0
            for y in a[i: k + 1]:
                x ^= y
            if x == 0:

                for j in range(i + 1, k + 1):
                    if (i, j, k) not in s:
                        s.add((i, j, k))
                        c += 1

    print(c)
