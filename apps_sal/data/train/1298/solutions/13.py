n = int(input())
while n != 0:
    k = int(input())
    l = list(map(int, input().split(' ')))
    k = l[0]
    c = 0
    for i in l:
        if i > k:
            c += 1
    print(c)
    n -= 1
