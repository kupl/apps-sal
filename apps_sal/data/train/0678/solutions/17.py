t = int(input())
while t > 0:
    n = int(input()) - 1
    l = list(map(int, input().split()))
    l1 = []
    c = 0
    for i in l:
        c += i
        l1.append(c)
    i = 0
    c = 0
    while n > 0:
        n = n - l1[i]
        i = i + l1[i]
        c += 1
    print(c)
    t -= 1
