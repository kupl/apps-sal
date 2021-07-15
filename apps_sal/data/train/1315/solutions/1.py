try:
    s=[]
    for i in range(int(input())):
        n=list(map(int,input().split()))
        n.sort()
        s.append(n)
    unique=[]
    for i in s:
        if(s.count(i)==1):
            unique.append(i)
        else:
            continue
    print(len(unique))
            
except:
    pass
