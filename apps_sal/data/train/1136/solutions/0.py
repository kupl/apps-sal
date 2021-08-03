
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if n == 1:
        print(m)
    else:

        if n % 2 == 0:
            print((n // 2) * m)

        else:
            print(((n // 2) + 1) * m)
