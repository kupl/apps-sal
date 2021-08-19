t = int(input())
l = []
while t:
    q = input()
    l = q.split()
    n = int(l[0])
    k = int(l[1])
    if n % 2 == 0:
        print(int(n / 2 + n / 2 * (1 + k)))
    else:
        print(int(n // 2 + n // 2 * (1 + k) + 1 + 2 * k))
    t = t - 1
