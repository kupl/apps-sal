import sys

for _ in range(int(sys.stdin.readline())):
    l=int(sys.stdin.readline())
    a=sys.stdin.readline().split()
    a=list(map(int,a))
    t=set(a)
    count=[]
    c=[]
    if len(t)==len(a):
        print(min(a),1)
        
    elif len(t)==1:
        print(a[0],l)
        
    else:
        for j in t:
            c.append(j)
        c.sort()
        for i in c:
            num=a.count(i)
            count.append(num)
            
        times=max(count)
        index=count.index(times)
        print(c[index],times)
            
    
