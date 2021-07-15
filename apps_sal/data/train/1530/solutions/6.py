# cook your dish here
for u in range(int(input().strip())):
    n = int(input().strip())
    k = 1
    for i in range(1,n+1):
        l = list()
        
        for j in range(1,i+1):
            l.append(k)
            k +=1
        print(*l[::-1],sep='')
        print()
        l.clear()
