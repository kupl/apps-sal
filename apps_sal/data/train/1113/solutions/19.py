# codechef - february 2012 - count of maximum - maxcount.py

t = int(input())

for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    for elem in a:
        if elem in c:
            c[elem]+=1
        else:
            c[elem]=1

    bestCount = 0
    best = 0
    for elem in c:
        if c[elem]>bestCount:
            bestCount=c[elem]
            best = elem
        elif c[elem]==bestCount and elem<best:
            best = elem
            
    print(best, bestCount)

