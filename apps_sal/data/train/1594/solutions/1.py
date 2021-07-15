t = int(input())
for i in range(t):
    n = int(input())
    l =[]
    for j in range(n):
        l.append(list(input()))
    if(n==1):
        print(1)
        continue
    elif(n==2):
        print(3)
        continue
    else:
        val = int((n*(n+1))/2)
        count = (n-3)+1
        flagl = 1
        flagr = 1
        for j in range(n):
            if(flagl==0 and flagr==0):
                break
            if(l[j][j]=='0'):
                flagl=0
            if(l[n-j-1][n-j-1]=='0'):
                flagr=0
        if(flagl==0 and flagr==0):
            print(val-count)
        else:
            print(val)

