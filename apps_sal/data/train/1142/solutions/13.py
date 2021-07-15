try:
    t=int(input())
    l=[]
    for _ in range(t):
        f=int(input())
        l.append(f)
        l.sort(reverse=True)
        print(l.index(f)+1)
except:
    pass
