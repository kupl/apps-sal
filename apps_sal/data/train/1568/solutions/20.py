t=int(input())
for i in range(t):
    n=int(input())
    ct=0
    inputdata=input()
    a=inputdata.split()
    a=[int(c) for c in a]
    
    for i in a:
        if (i>=n/2):
            ct=ct+1
    
    print(ct)
