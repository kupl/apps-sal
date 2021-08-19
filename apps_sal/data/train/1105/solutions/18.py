try:
    t = int(input())
except:
    t = 0
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    b1 = b2 = 0
    for i in l:
        if b1 < b2:
            b1 += i
        else:
            b2 += i
    print(max(b1, b2))
