t=eval(input())
for i in range(0,t):
    x=input()
    nm=x.split(' ')
    nm[0]=int(nm[0])
    nm[1]=int(nm[1])
    csoint=[]
    lsoint=[]
    csofloat=[]
    lsofloat=[]
    for j in range(0,nm[0]):
        a=input()
        b=a.split(' ')
        b[0]=int(b[0])
        b[1]=int(b[1])
        csoint.append(b[0])
        lsoint.append(b[1])
    for k in range(0,nm[1]):
        a=input()
        b=a.split(' ')
        b[0]=int(b[0])
        b[1]=int(b[1])
        csofloat.append(b[0])
        lsofloat.append(b[1])
    chakra=0

##    for j in range(0,nm[0]):
##        if csofloat==[0]*nm[1]:
##                print chakra
##                break
##        for k in range(0,nm[1]):
##            if csofloat==[0]*nm[1]:
##                print chakra
##                break
##            if lsoint[j]==lsofloat[k]:
##                if csoint[j]>csofloat[k]:
##                    csoint[j]-=csofloat[k]
##                    csofloat[k]=0
##                    lsofloat[k]=0
##                elif csofloat[k]>csoint[j]:
##                    if lsoint.count(lsoint[j])==1==lsofloat.count(lsofloat[k]):
##                        chakra+=csofloat[k]-csoint[j]
##                        csoint[j]=csofloat[k]
##                        csoint[j]=0
##                        csofloat[k]=0
##                        lsoint[j]=0
##                        lsofloat[k]=0
##                    elif lsoint.count(lsoint[j])==1 and lsofloat.count(lsofloat[k])>lsoint.count(lsoint[j]):
##                        csoint[j]=csofloat[k]+1
##                        chakra+=csofloat[k]-csoint[j]+1
##                        csoint[j]=1
##                        csofloat[k]=0
##                        lsofloat[k]=0
##                    else:
##                        csofloat[k]-=csoint[j]
##                        csoint[j]=0
##                        lsoint[j]=0
##                        break
##                else:
##                    if lsoint.count(lsoint[j])==1 and lsoint.count(lsoint[j])>=lsofloat.count(lsofloat[k]):
##                        csoint[j]=0
##                        csofloat[k]=0
##                        lsoint[j]=0
##                        lsofloat[k]=0
##                        break
##                    elif lsoint.count(lsoint[j])==1 and lsoint.count(lsoint[j])<lsofloat.count(lsofloat[k]):
##                        csoint[j]=1
##                        chakra+=1
##                        csofloat[k]=0
##                        lsofloat[k]=0
    l=min(lsoint)-1
    ci=[]
    for a in range(l+1,max(lsoint)+1):
        c=0
        l+=1
        if l not in lsoint:
            continue
        for j in range(0,nm[0]):
           if lsoint[j]==l:
               c+=csoint[j]
        ci.append(c)
    
    l=min(lsofloat)-1
    cf=[]
    for a in range(l+1,max(lsofloat)+1):
        c=0
        l+=1
        if l not in lsofloat:
            continue
        for j in range(0,nm[1]):
            if lsofloat[j]==l:
                c+=csofloat[j]
        cf.append(c)

    for i in range(0,len(ci)):
        if ci[i]<cf[i]:
            chakra+=cf[i]-ci[i]
    print(chakra)

