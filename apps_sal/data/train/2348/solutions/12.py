def main():
    n = int(input())
    x = list(map(int, input().split()))
    l = int(input())
    q = int(input())
    ab = [list([int(x) - 1 for x in input().split()]) for _ in [0] * q]
    doubling = [[] for _ in [0] * n]
    j = 0
    for i in range(n):
        while j < n:
            if x[j] - x[i] > l:
                doubling[i].append(j - 1)
                break
            else:
                j += 1
    for i in range(n - 1, -1, -1):
        if not doubling[i]:
            doubling[i].append(n - 1)
        else:
            break
    for _ in range(16):
        for i in range(n):
            doubling[i].append(doubling[doubling[i][-1]][-1])
    for a, b in ab:
        if a > b:
            a, b = b, a
        ans = 0
        j = 16
        while j >= 0:
            if doubling[a][j] >= b:
                j -= 1
            else:
                a = doubling[a][j]
                ans += 2**j
        if a == b:
            print(ans)
        else:
            print((ans + 1))


main()
