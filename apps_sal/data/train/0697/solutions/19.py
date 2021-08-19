def main():
    for _ in range(int(input())):
        (n, k) = list(map(int, input().split()))
        a = list(map(int, input().split()))
        s = sum(a[:k])
        m = s
        for i in range(k, n):
            m = max(m, s + a[i] - a[i - k])
            s = s + a[i] - a[i - k]
        print(m)


main()
