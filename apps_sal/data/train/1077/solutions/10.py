def __starting_point():
    ntc=int(input())
    c=0
    res=[]
    while c<ntc:
        ro=[]
        di=[]
        n=int(input())
        c1=0
        res.append([])
        res[c].append("")
        while c1<n:
            var=input()
            a=var.index("on")
            ro.append(var[a+3:])
            a=var.index(" ")
            di.append(var[:a])
            c1+=1
        c1=n-2
        res[c][0]="Begin on " +ro[n-1]
        while c1>=0:
             if di[c1+1]=="Left":
                 res[c].append("Right")
             elif di[c1+1]=="Right":
                 res[c].append("Left")
             res[c][n-1-c1]=res[c][n-1-c1]+" "+"on"+" "+ro[c1]
             c1-=1
             
        c+=1
    c=0    
    while c<ntc:
        l=len(res[c])
        c1=0
        while(c1<l):
            print(res[c][c1])
            c1+=1
        c+=1
        
    
    

             
             
            
            
            
            
        

__starting_point()
