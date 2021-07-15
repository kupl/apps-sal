try:
    tc=int(input())
    for _ in range(tc):
        n=int(input())
        st=""
        b=1
        for i in range(1,n+1):
            b+=1
            a=b
            for j in range(1,n+1):
                print(a,end='')
                a+=1
            print()        
except:
    pass
