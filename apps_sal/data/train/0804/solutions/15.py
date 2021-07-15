try:
    t=int(input())
    for i in range(t):
        
        
        n=int(input())
        a=list(map(int,input().split()))
        a1=a.copy()
        #print("a1==",a1)
        f=int(input())
        length_a=len(a)
        #print(min(l))
        l1=[]
        l2=[]
        
        
        
        
        for j in range(length_a+1):
                a=a1.copy()
                
                #print("1st line with j",a,j)
                l=['D',0,0]
                a.insert(j,l)
                k=0
                l[2]=j+1
                #print(a)
                while len(a) !=2:
                    length=len(a)
                    #print("****",length,k)
                    if k>=length:
                        k=0
                    if a[k]==l:
                        k=k+1
                        #print("skipped")
                        continue
                    else:
                        m=k+1
                        if m>=length:
                            m=0
                        if a[m]==l:
                            l[1]+=a[k]
                        else:
                            del a[m]
                            #print("a[m] wala",a)
                        k+=1
                    
                '''if len(a)==2:
                    if a[0]==l:
                        l[1]+=f
                    else:
                        a[1]=a[1]-f
                        
                    if a[1]==l:
                        l[1]+=f
                    else:
                        a[0]=a[0]-f
                        if a[0]<0:
                            l1.append(l)
                ''' 
                
                if a[0]==l:
                    l[1]+=f
                        
                else:
                        a[0]=a[0]-f
                if a[1]==l:
                    l[1]+=f
                        
                else:
                        a[1]=a[1]-f
                #print("z wala loop",a)
                
                if a[0]!=l:
                        if a[0]<=0:
                            l1.append(l)
                            l2.append(1)
                        else:
                            l2.append(0)
                if a[1]!=l:
                        if a[1]<=0:
                            l1.append(l)
                            l2.append(1)
                        else:
                            l2.append(0)
                #print("l1,l2",l1,l2)
                
                #print("last line->>",a)
        '''if 1 in l2:
                value=min(l1)
                print('possible')
                
                print(value[2],value[1])
        else:
                print('impossible')
                '''
        if len(l1)>0:
            value=min(l1)
            print('possible')
                
            print(value[2],value[1])
        else:
            print('impossible')
except:
    pass
