t=int(input())
while t>0:
    li1=[int(i) for i in input().split()]
    li2=[int(i) for i in input().split()]
    s1=set()
    s2=set()
    val,ans=0,3
    for i in range(3):
        if li1[i]==li2[i]:
            val+=1
    if val==3:
        ans=0
    elif val==2:
        ans=1
    else:
        for i in range(3):
            if li2[i]-li1[i]!=0:
                s1.add(li2[i]-li1[i])
            if li1[i]!=0 and li2[i]%li1[i]==0 and li2[i]//li1[i]!=1:
                s2.add(li2[i]//li1[i])
        temp=[]
        for i in s1:
            for j in range(7):
                temp=[li1[k] for k in range(3)]
                if j==0:
                    temp[0]+=i
                    temp[1]+=i
                elif j==1:
                    temp[0]+=i
                    temp[2]+=i
                elif j==2:
                    temp[1]+=i
                    temp[2]+=i
                elif j==3:
                    temp[0]+=i
                    temp[1]+=i
                    temp[2]+=i
                elif j==4:
                    temp[0]+=i
                elif j==5:
                    temp[1]+=i
                elif j==6:
                    temp[2]+=i
                a=0
                for k in range(3):
                    if temp[k]==li2[k]:
                        a+=1
                if a==3:
                    ans=1
                if a==2:
                    ans=min(ans,2)
                s3=set()
                for k in range(3):
                    if temp[k]!=0 and li2[k]%temp[k]==0 and li2[k]//temp[k]!=1:
                        s3.add(li2[k]//temp[k])
                temp1=[]
                for k in s3:
                    for l in range(7):
                        temp1=[temp[m] for m in range(3)]
                        if l==0:
                            temp1[0]*=k
                            temp1[1]*=k
                        elif l==1:
                            temp1[0]*=k
                            temp1[2]*=k
                        elif l==2:
                            temp1[1]*=k
                            temp1[2]*=k
                        elif l==3:
                            temp1[0]*=k
                            temp1[1]*=k
                            temp1[2]*=k
                        elif l==4:
                            temp1[0]*=k
                        elif l==5:
                            temp1[1]*=k
                        elif l==6:
                            temp1[2]*=k
                        for m in range(3):
                            if li2[m]!=temp1[m]:
                                break
                            if m==2:
                                ans=min(ans,2)
                s4=set()
                for k in range(3):
                    if li2[k]-temp[k]!=0:
                        s4.add(li2[k]-temp[k])
                temp2=[]
                for k in s4:
                    for l in range(7):
                        temp2=[temp[m] for m in range(3)]
                        if l==0:
                            temp2[0]+=k
                            temp2[1]+=k
                        elif l==1:
                            temp2[0]+=k
                            temp2[2]+=k
                        elif l==2:
                            temp2[1]+=k
                            temp2[2]+=k
                        elif l==3:
                            temp2[0]+=k
                            temp2[1]+=k
                            temp2[2]+=k
                        elif l==4:
                            temp2[0]+=k
                        elif l==5:
                            temp2[1]+=k
                        elif l==6:
                            temp2[2]+=k
                        for m in range(3):
                            if li2[m]!=temp2[m]:
                                break
                            if m==2:
                                ans=min(ans,2)
                s4.clear()
                count=0
                for k in range(3):
                    var=li2[k]-i
                    if li1[k]!=0 and var%li1[k]==0:
                        if var//li1[k]!=1:
                            s4.add(var//li1[k])
                        count+=1
                if len(s4)==1 and count==3:
                    ans=min(ans,2)
        if ans==3 or ans==2:
            d1=li2[2]-li2[1]
            d2=li2[1]-li2[0]
            d3=li1[2]-li1[1]
            d4=li1[1]-li1[0]
            d5=li2[2]-li2[0]
            d6=li1[2]-li1[0]
            if (d3!=0 and d4!=0 and d6!=0 and d1%d3==0 and d2%d4==0 and d5%d6==0 and d1//d3==d2//d4 and d1//d3==d5//d6):
                ans=min(ans,2)
            for i in s2:
                s3=set()
                count=0
                for j in range(3):
                    temp[j]=li2[j]
                    if i!=0 and temp[j]%i==0:
                        temp[j]//=i
                        temp[j]-=li1[j]
                        if temp[j]!=0:
                            s3.add(temp[j])
                        count+=1
                    
                if len(s3)==1 and count==3:
                    ans=min(ans,2)
            for i in s2:
                for j in range(7):
                    temp=[li1[k] for k in range(3)]
                    if j==0:
                        temp[0]*=i
                        temp[1]*=i
                    elif j==1:
                        temp[0]*=i
                        temp[2]*=i
                    elif j==2:
                        temp[1]*=i
                        temp[2]*=i
                    elif j==3:
                        temp[0]*=i
                        temp[1]*=i
                        temp[2]*=i
                    elif j==4:
                        temp[0]*=i
                    elif j==5:
                        temp[1]*=i
                    elif j==6:
                        temp[2]*=i
                    a=0
                    for k in range(3):
                        if temp[k]==li2[k]:
                            a+=1
                    if a==3:
                        ans=1
                    elif a==2:
                        ans=min(ans,2)
                    temp2=[]
                    s4=set()
                    for k in range(3):
                        if temp[k]!=0 and li2[k]%temp[k]==0 and li2[k]//temp[k]!=1:
                            s4.add(li2[k]//temp[k])
                    temp2=[]
                    for k in s4:
                        for l in range(7):
                            temp2=[temp[m] for m in range(3)]
                            if l==0:
                                temp2[0]*=k
                                temp2[1]*=k
                            elif l==1:
                                temp2[0]*=k
                                temp2[2]*=k
                            elif l==2:
                                temp2[1]*=k
                                temp2[2]*=k
                            elif l==3:
                                temp2[0]*=k
                                temp2[1]*=k
                                temp2[2]*=k
                            elif l==4:
                                temp2[0]*=k
                            elif l==5:
                                temp2[1]*=k
                            elif l==6:
                                temp2[2]*=k
                            for m in range(3):
                                if li2[m]!=temp2[m]:
                                    break
                                if m==2:
                                    ans=min(ans,2)
                    s4.clear()
                    for k in range(3):
                        var=li2[k]-temp[k]
                        if var!=0:
                            s4.add(var)
                    if len(s4)==1:
                        ans=min(ans,2)
    print(ans)
    t-=1

