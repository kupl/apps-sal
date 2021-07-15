try:
    n=int(input())
    for i in range(0,n):
        a=int(input())
        b=input().split()
        counta=0
        countb=0
        for j in range(a-1,-1,-1):
            if(b[j]=='0'):
                countb=countb+1
            else:
                break
        for k in range(0,a):
            if(b[k]=='0'):
                counta=counta+1
            else:
                break
            
        count=counta+countb
        if(count<a):
            print(a-count)
        else:
            print(1)
except:
    pass
