# cook your dish here
n = int(input())
if n == 0:
    print(0)
else:
    l = [[0 for i in range(2 * n - 1)] for j in range(2 * n - 1)]
    for i in range(1, 2 * n):
        k = []
        for j in range(1, 2 * n):
            d = max(abs(i - n), abs(j - n))
            k.append(d + 1)
        print(*k)
