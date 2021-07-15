try:
    t=int(input())
    for _ in range(t):
        n=int(input())
        l=[int(x) for x in input().split()]
        temp=[0]*n
        s=set()
        for ele in l:
            if ele not in s:
                s.add(ele)
        for i in range(n):
            l[i]=0
        
        for i in range(0,n):
            if i in s:
                l[i]=i
        print(*l) 
except EOFError:
    pass
