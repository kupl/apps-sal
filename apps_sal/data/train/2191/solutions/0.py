def main():
    input()
    aa = sorted(map(int, input().split()))
    maxa = max(aa)
    m = [False] * (maxa + 1)
    x = []
    b = 0
    for a in aa:
        if b != a:
            m[a] = True
            for i in range(b, a):
                x.append(b)
            b = a
    x.append(b)
    ans = 0
    for i in range(maxa - 1, 1, -1):
        if i < ans:
            break
        if m[i]:
            for j in range(1, maxa // i + 1):
                ans = max(ans, x[min(i * (j + 1) - 1, maxa)] % i)
    print(ans)


def __starting_point():
    main()
__starting_point()
