# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    lower ={}
    upper ={}
    points ={}
    for j in range(N):
        lower[j],upper[j] = map(int,input().split()) 
        points[j] = 0
    for p in range(N):
        for m in range(p+1,N):
            if (lower[p]<lower[m] and upper[p]>=upper[m]) or (lower[p]<=lower[m] and upper[p]>upper[m]):
                points[p] += 2
            elif (lower[p]>lower[m] and upper[p]<=upper[m]) or (lower[p]>=lower[m] and upper[p]<upper[m]):
                points[m] += 2
            else:
                points[p] +=1
                points[m] +=1
    for n in range(N):
        print(points[n],end=" ")
    print()
