# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n == 1:
        print(k)
    else:
        if (n % 2) != 0:
            print((n // 2 + 1) * k)
        else:
            print(n // 2 * k)
