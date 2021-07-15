t = int(input())

for _ in range(t):
    n = int(input())
    ppl = list(input())
    d = int(input())
    toiso = list(map(int, input().split()))
    
    iso = []
    iso.append(toiso[0])
    l = []
    r = []
    c = 0
    tl = []
    tr = []

    for i in range(n):
        if (ppl[i]=='1'):
            l.append(i)
            r.append(i)
            c+=1
    
    for i in range(d):
        ll = len(l)
        for j in range(ll):
            if ((l[j]-1)>=0):
                if ((ppl[l[j]-1]=='0') and ((l[j]+1) not in iso)):
                    ppl[l[j]-1]='1'
                    l.append(l[j]-1)
                    c+=1
        l = l[ll:]
        # print("l", l)

        rr = len(r)
        for j in range(rr):
            if ((r[j]+1)<n):
                if ((ppl[r[j]+1]=='0') and ((r[j]+2) not in iso)):
                    ppl[r[j]+1]='1'
                    r.append(r[j]+1)
                    c+=1
        r = r[rr:]
        # print("r", r)
        
        if (i!=(d-1)):
            iso.append(toiso[i+1])
    
    print(c)
