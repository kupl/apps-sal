t=int(input())
while t:
    k,n=map(int,input().split())
    l=[]
    j=0
    h=k
    while h:
        p=list(map(int,input().split()))
        l.append(p)
        h-=1
    if k>3:
        j=1
    elif k==1:
        if (l[0][0]==0 and l[0][1]==n-1) or (l[0][0]==0 and l[0][1]==0) or (l[0][0]==n-1 and l[0][1]==0) or (l[0][0]==n-1 and l[0][1]==n-1):
            j=1
    elif k==2:
        for q in range(2):
            if (l[q][0]==0 and l[q][1]==n-1) or (l[q][0]==0 and l[q][1]==0) or (l[q][0]==n-1 and l[q][1]==0) or (l[q][0]==n-1 and l[q][1]==n-1):
                j=1
        if l[0][0]==0 or l[0][0]==n-1:
            if l[1][0]==0 or l[1][0]==n-1: 
                j=1
        if l[0][1]==0 or l[0][1]==n-1:
            if l[1][1]==0 or l[1][1]==n-1: 
                j=1
    elif k==3:
        for q in range(3):
            if (l[q][0]==0 and l[q][1]==n-1) or (l[q][0]==0 and l[q][1]==0) or (l[q][0]==n-1 and l[q][1]==0) or (l[q][0]==n-1 and l[q][1]==n-1):
                j=1
        for q in range(2):
            for w in range(q+1,3):
                if l[q][0]==0 or l[q][0]==n-1:
                    if l[w][0]==0 or l[w][0]==n-1: 
                        j=1
                if l[q][1]==0 or l[q][1]==n-1:
                    if l[w][1]==0 or l[w][1]==n-1:
                        j=1
                if l[q][0]==0 or l[q][0]==n-1:
                    if l[w][1]==0 or l[w][1]==n-1:
                        j=1
                if l[q][1]==0 or l[q][1]==n-1:
                    if l[w][0]==0 or l[w][0]==n-1:
                        j=1
        for q in range(3):
            w=(q+1)%3
            r=(q+2)%3
            if l[q][0]==0 or l[q][0]==n-1:
                if (l[q][1]-l[w][1])*(l[q][1]-l[r][1])>=0:
                    j=1
            if l[q][1]==0 or l[q][1]==n-1:
                if (l[q][0]-l[w][0])*(l[q][0]-l[r][0])>=0:
                    j=1
    if j:
        print("yes")
    else:
        print("no")
    t-=1
