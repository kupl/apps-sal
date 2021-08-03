for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l.sort()

    c = 0
    mn = abs(l[0] + l[1] - k)
    for i in range(n - 1):
        for j in range(i + 1, n):
            temp = abs(l[i] + l[j] - k)
            if temp == mn:
                c += 1

            elif temp < mn:
                mn = temp
                c = 1

            elif l[i] + l[j] - k > mn:
                break

    print(mn, c)
