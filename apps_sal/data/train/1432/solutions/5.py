try:
    t = int(input())
    for _ in range(t):
        N = int(input())
        c = 0
        p = N-1
        a = [100 for i in range(N)]
        a[0] = N 
        for i in range(1,N):
            a[i] = a[i-1]+2*p 
            p-=1 
        for j in range(N):
            row = input().split(' ')
            for k in range(N):
                if int(row[k]) == 1:
                    c+=1 
        for i in range(N):
            if c <= a[i]:
                print(i)
                break
except:
    pass
        
    

