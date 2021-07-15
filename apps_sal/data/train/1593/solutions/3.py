for _ in range(int(input())):
    l=[100,50,10,5,2,1]
    n=int(input())
    c=0
    for i in l:
        if(n>=i):
            r=n/i
            if(type(r)==int):
                print(r)
                break
            else:
                r=int(r)
                c+=r
                n=n-(i*r)
        if(n==0):
            break
    print(c)
            
                    
                
            
            

