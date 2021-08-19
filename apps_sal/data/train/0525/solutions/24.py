n = int(input())
for i in range(n):
    l = list(map(int, input().split(' ')))
    p = 0
    k = 0
    while p <= l[2]:
        m = p
        p = l[0] * k + l[1]
        k += 1
    print(m)
