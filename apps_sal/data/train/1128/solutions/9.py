l = []
n = int(input())
for i in range(0, n):
    s = int(input())
    l = []
    l = list(map(int, input().split()))
    beg = 0
    suml = 0
    sumr = 0
    for j in range(0, len(l)):
        sumr = sumr + l[j]
    for j in range(0, len(l)):
        sumr = sumr - l[j]
        if sumr == suml:
            print(j)
            beg = 1
            break
        suml = suml + l[j]
    if beg == 0:
        print(-1)
