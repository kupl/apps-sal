for _ in range(int(input())):
    l, r = map(int, input().split())
    r = r - 1
    n = r // l
    sum_ = n * (2 * l + (n - 1) * l)
    print(sum_ // 2)
