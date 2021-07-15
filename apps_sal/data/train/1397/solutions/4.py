for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    u = list(set(l))
    u.sort()
    d ={}
    for i in u:
        d[i] = []
    for i in range(n):
        d[l[i]].append(i)
    f = d[u[0]][0]
    p = 1
    m = 1
    while p < len(u):
        if d[u[p]][-1]>f:
            for j in d[u[p]]:
                if j>f:
                    f = j
                    p+=1
                    break
        else:
            m += 1
            f = d[u[p]][0]
            p+=1
    print(m)
    
    
                
                
                

