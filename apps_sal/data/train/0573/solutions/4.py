T = int(input())
for i in range(T):
    (n, m) = input().split(' ')
    n = int(n)
    m = int(m)
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(n + 2 * m - 3)
