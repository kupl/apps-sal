t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    for i in range(1, n):
        a = a + i * i * i
    a = 2 * a
    a = a + n * n * n
    print(a)
