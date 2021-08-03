t = int(input())
while(t != 0):
    n, m = map(int, input().split(" "))
    l = [10] * (n)
    for i in range(m):
        l1, r, p = map(int, input().split(" "))
        for k in range(l1 - 1, r):
            l[k] = l[k] * p
    print(sum(l) // len(l))
    t -= 1
