# cook your dish here
sam = int(input())

for i in range(sam):
    csk,mi,dam,man = int(input()),list(map(int,list(input()))),int(input()),list(map(int,input().split()))
    
    mi.insert(0,"|"),mi.append("|")
    pj = []
    for i in range(1,csk+1):
        if(mi[i]==1):
            pj.append(i)
    
    i = 0
    while(i<dam):
        boundary = man[i] + i
        mi.insert(boundary,"|")
        times = len(pj)
        for p in range(times):
            index = pj[p]
            if(index>=boundary):
                index+=1
                pj[p]+=1
            if(mi[index]==1):
                if(mi[index+1]==0):
                    mi[index+1] = 1
                    pj.append(index+1)
                if(mi[index-1]==0):
                    mi[index-1] = 1
                    pj.append(index-1)
            else:
                pj.remove(index)
                times=times-1
        i=i+1
        pj.sort()
    
    print(mi.count(1))

