T = int(input())
for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    maxi = 0
    index_min = 0
    ratmax = 0
    for j in range(N):
        prod = l[j] * r[j]
        if(prod > maxi):
            maxi = prod
            index_min = j
            ratmax = r[j]
        elif(prod == maxi):
            if(r[j] > ratmax):
                ratmax = r[j]
                index_min = j
    print(index_min + 1)
