t = int(input())
for _ in range(0, t):
    n, m = input().split()
    n, m = int(n), int(m)
    if m != n:
        print("-1 -1")
    else:
        for i in range(0, n):
            if i + 2 <= n:
                print(i + 1, i + 2)
            else:
                print(i + 1, "1")
