for _ in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    if(a==b):
        print('YES')
    elif(c==d):
        print('NO')
    
    else:
        if(abs(a-b)%abs(c-d)==0):
            print('YES')
        else:
            print('NO')

