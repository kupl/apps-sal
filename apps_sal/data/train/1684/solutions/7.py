def fun(n):
    for i in range(n):
        if i != n - 1:
            print(n, end=' ')
        else:
            print(n)


t = int(input())
for _ in range(t):
    n = int(input())
    fun(n)
