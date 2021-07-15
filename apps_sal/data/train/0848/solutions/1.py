def func(n,l):
    if(n<=3):
        return sum(l)
    else:
        s=0
        for i in range(n-2):
            temp = sum(l[i:i+3:])
            if(temp>s):
                s = temp
        temp = l[n-1]+l[0]+l[1]
        if(temp>s):
                s = temp
        temp = l[n-1]+l[n-2]+l[0]
        if(temp>s):
                s = temp
        
        return s
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(func(n,l))
    

